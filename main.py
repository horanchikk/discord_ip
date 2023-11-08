from fastapi import FastAPI, Request
from fastapi.responses import FileResponse

from image import make_spanchbob


app = FastAPI()



@app.get('/user{id}')
async def get_user_by_id(id: int, req: Request):
    img = make_spanchbob(f'{req.client.host}')
    img.save(f'{req.client.host}.jpg', 'JPEG')
    return FileResponse(f'{req.client.host}.jpg')
