from fastapi import FastAPI
import router
import asyncio

app = FastAPI()


@app.get('/')
async def Home():
    return {"message": 'Hello home'}

app.include_router(router.router)
asyncio.create_task(router.consume())