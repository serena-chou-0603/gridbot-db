from typing import List
import uvicorn
import fastapi as _fastapi
import os

# from aiogram import Bot, Dispatcher, types
import sqlalchemy.orm as _orm
from dotenv import load_dotenv

load_dotenv(".env")

# from telegram_bot import dp, bot
import services as _services
import pprint
import schemas as _schemas
from routers.users import usersRouter
from routers.dcabots import dcabotsRouter
from routers.gridbots import gridbotsRouter
from routers.profits import profitsRouter
from routers.hourprofits import hourprofitsRouter
from routers.dcatrans import dcatransRouter

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
TELEGRAM_WEBHOOK_PATH = f"/bot/{TELEGRAM_TOKEN}"
TELEGRAM_WEBHOOK_URL = "https://fa78-118-167-143-30.ngrok.io" + TELEGRAM_WEBHOOK_PATH

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


# @app.on_event("startup")
# async def on_startup():
# webhook_info = await bot.get_webhook_info()
# if webhook_info.url != WEBHOOK_URL:
#    await bot.set_webhook(
#        url=WEBHOOK_URL
#    )
#    await bot.set_webhook(TELEGRAM_WEBHOOK_URL)


# @app.post(TELEGRAM_WEBHOOK_PATH)
# async def bot_webhook(update: dict):
#    telegram_update = types.Update(**update)
#    pprint.pprint(telegram_update)
#    # Dispatcher.set_current(dp)
#    Bot.set_current(bot)
#    await dp.process_update(telegram_update)
#    # 必須返回 200，當 telegram 收到此以外的數值會嘗試重新傳送訊息導致卡住。
#    # return response.empty(200)


# @app.on_event("shutdown")
# async def on_shutdown():
#    # await bot.session.close()
#    await bot.delete_webhook()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
