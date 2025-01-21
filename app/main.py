from fastapi import FastAPI, Request
from greenlet import greenlet
from prometheus_client import make_asgi_app, Counter, Histogram
import uuid
import logging
from sqlalchemy import text


from sqlalchemy.ext.asyncio import create_async_engine

from config.settings import settings
from .api.crud_post.router import router as crud_router
from .api.tech.router import router as tech_router
from .api.games.router import router as games_router
from .metrics import REQUEST_COUNT_2XX, logger, REQUEST_COUNT_3XX, REQUEST_COUNT_4XX, REQUEST_COUNT_5XX, measure_latency

metrics_app = make_asgi_app()

logging.basicConfig(level=logging.INFO)

app = FastAPI()

app.mount("/tech/metrics", metrics_app)

app.include_router(crud_router, prefix="/posts", tags=["posts"])
app.include_router(tech_router, prefix="/tech", tags=["tech"])
app.include_router(games_router, prefix="/games", tags=["games"])

@app.middleware("http")
async def add_correlation_id_and_count_requests(request: Request, call_next):
    correlation_id = request.headers.get('X-Correlation-ID', str(uuid.uuid4()))
    request.state.correlation_id = correlation_id
    response = await call_next(request)
    response.headers['X-Correlation-ID'] = correlation_id

    status_code = response.status_code
    if 200 <= status_code < 300:
        REQUEST_COUNT_2XX.inc()
    elif 300 <= status_code < 400:
        REQUEST_COUNT_3XX.inc()
    elif 400 <= status_code < 500:
        REQUEST_COUNT_4XX.inc()
    elif 500 <= status_code < 600:
        REQUEST_COUNT_5XX.inc()

    return response

@app.get("/")
@measure_latency("Processing request for root")
async def read_root(request: Request):
    return {"message": "Hello, World!"}


@app.get("/test-db")
async def test_db():
    engine = create_async_engine(settings.db_url)
    async with engine.connect() as connection:
        result = await connection.execute(text("SELECT 1"))
        return {"status": "success", "result": result.scalar()}