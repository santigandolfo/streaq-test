
from streaq import Worker
from collections.abc import AsyncGenerator
import asyncio

worker = Worker(
    concurrency=1,
    prefetch=0,
    redis_url="redis://redis:6379",
    priorities=['low', 'mid', 'high'],
)

async def get_worker() -> AsyncGenerator[Worker]:
    async with worker:
        yield worker

@worker.task()
async def task_low():
    await asyncio.sleep(5)


@worker.task()
async def task_mid():
    await asyncio.sleep(5)


@worker.task()
async def task_high():
    await asyncio.sleep(5)