from starlette.requests import Request
from starlette.responses import Response

from app.api.tech.router import router


@router.get('/healthcheck')
async def healthcheck(request: Request) -> Response:
    return Response('Healthy', status_code=200)
