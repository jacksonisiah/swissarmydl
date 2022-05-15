# https://community.sanicframework.org/t/websocket-with-class-based-views/761

class Downloads:
    async def websocket(request, ws):
        message = "Start"
        while True:
            await ws.send(message)
            message = await ws.recv()
