import os
from routes.downloads import Downloads
from sanic import Sanic

global app
app = Sanic('api')

app_port: int = os.getenv('API_PORT') or 8000
app.config.FORWARDED_SECRET = os.getenv('API_SECRET') or 'balls69'

app.static('/cache', './cache')
#app.add_route('/auth', '')
#app.add_route('/purge', '')
app.websocket(Downloads.websocket, '/ws')

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=app_port, workers=8, access_log=True)
