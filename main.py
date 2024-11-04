from fastapi import FastAPI, BackgroundTasks, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger
from routers import products, category, auth
from backend.config import redis_settings
from starlette.websockets import WebSocketDisconnect
from backend.managers import ConnectionManager

from celery import Celery


app = FastAPI()

# Добавляем логгер
logger.add('info.log')

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)


# Настройка Celery
celery = Celery(
    __name__,
    broker=redis_settings.url,
    backend=redis_settings.url,
    broker_connection_retry_on_startup=True
)

manager = ConnectionManager()


app.include_router(products.router)
app.include_router(category.router)
app.include_router(auth.router)


# Фоновая задача
def call_background_task():
    import time
    time.sleep(10)
    print('Background Task Called')


# Вызов фоновой задачи
@app.get('/')
async def hello_world(background_tasks: BackgroundTasks):
    background_tasks.add_task(call_background_task)
    return {'message': 'hello world'}


@celery.task
def call_background_task_celery(message):
    import time
    time.sleep(10)
    print('Background task called')
    print(message)


@app.get('/celery')
async def get_celery_task(message: str):
    call_background_task_celery.delay(message)
    return {'message': 'Call background task celery'}


# ws://127.0.0.1:8000/ws
@app.websocket('/ws')
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(data.upper())
    except WebSocketDisconnect as e:
        print(f'Connection closed {e.code}')


@app.websocket('/ws/{client_id}')
async def websocket_endpoint_client(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)

    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f'Client {client_id}: {data}')
    except WebSocketDisconnect as e:
        manager.connections.remove(websocket)
        print(f'Connection closed {e.code}')