import json

from fastapi import FastAPI, Request, WebSocket
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="")

@app.get("/")
async def get(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "data": "ola"}
        )


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    i = 0
    while True:
        i += 1
        data = await websocket.receive_text()
        encoded_data = json.loads(data)
        encoded_data["num"] = i
        decoded_data = json.dumps(encoded_data)
        await websocket.send_text(decoded_data)



