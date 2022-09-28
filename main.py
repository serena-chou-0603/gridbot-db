from typing import List
import uvicorn
import fastapi as _fastapi
import sqlalchemy.orm as _orm
from dotenv import load_dotenv

load_dotenv(".env")

import services as _services
import schemas as _schemas
from routers.users import usersRouter
from routers.dcabots import dcabotsRouter
from routers.gridbots import gridbotsRouter
from routers.profits import profitsRouter
from routers.hourprofits import hourprofitsRouter
from routers.dcatrans import dcatransRouter

app = _fastapi.FastAPI()
_services.create_database()


app.include_router(usersRouter)
app.include_router(dcabotsRouter)
app.include_router(dcatransRouter)
app.include_router(gridbotsRouter)
app.include_router(profitsRouter)
app.include_router(hourprofitsRouter)


@app.post("/webhook", tags=["webhook"])
async def webhook(request: _fastapi.Request):
    body = await request.json()
    print(body)
    return body


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
