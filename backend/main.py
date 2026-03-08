from fastapi import FastAPI, WebSocket
from backend.websocket_server import websocket_endpoint

app = FastAPI()

@app.get("/")
def health_check():
    return {"status": "Voice AI Agent running"}

@app.websocket("/ws")
async def websocket_route(websocket: WebSocket):
    await websocket_endpoint(websocket)