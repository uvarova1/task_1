import random
from app.api.games.router import router
from app.metrics import measure_latency
from starlette.requests import Request

from app.metrics import HEADS_COUNTER, TAILS_COUNTER, FLIPS_COUNTER


@router.get('/coin-flip')
@measure_latency("Processing request for coin flip")
async def coin_flip(request: Request, times: int):
    heads = 0
    for _ in range(times):
        if random.randint(0, 1):
         heads += 1

    tails = times - heads

    HEADS_COUNTER.inc(heads)
    TAILS_COUNTER.inc(tails)
    FLIPS_COUNTER.inc(times)
    return {
        'heads': heads,
        'tails': tails
    }