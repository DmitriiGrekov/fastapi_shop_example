from fastapi import FastAPI, WebSocket, Request
from typing import List


class ConnectionManager:
    def __init__(self):
        self.connections: List[WebSocket] = []
        print('Creating a list to active connections', self.connections)

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.connections.append(websocket)
        print('New Active connections are ', self.connections)

    async def broadcast(self, data: str):
        for connection in self.connections:
            await connection.send_text(data)
            print('In broadcast: sent msg to ', connection)
