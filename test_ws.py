import asyncio
import websockets

async def test():
    uri = "ws://127.0.0.1:8000/ws"

    async with websockets.connect(uri) as websocket:

        # send audio filename to server
        await websocket.send("sample_agent.m4a")

        response = await websocket.recv()

        print("Server response:", response)

asyncio.run(test())