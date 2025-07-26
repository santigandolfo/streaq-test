from fastapi import FastAPI
from fastapi import Depends, Request, Response
from fastapi import status
from worker import get_worker, task_low, task_mid, task_high

app = FastAPI()

@app.get('/enqueue-tasks', dependencies=[Depends(get_worker)])
async def aaa(request: Request) -> Response:
    for _ in range(100):
        await task_low.enqueue().start(priority='low')
        await task_mid.enqueue().start(priority='mid')
        await task_high.enqueue().start(priority='high')
    return Response(status_code=status.HTTP_202_ACCEPTED)