from typing import List
import fastapi as _fastapi
import sqlalchemy.orm as _orm
import services as _services
import schemas as _schemas

gridbotsRouter = _fastapi.APIRouter()


@gridbotsRouter.post(
    "/users/{user_id}/bots/", response_model=_schemas.Bot, tags=["Bot Methods"]
)
def create_bot(
    user_id: int,
    bot: _schemas.BotCreate,
    db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    db_user = _services.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise _fastapi.HTTPException(
            status_code=404, detail="sorry this user does not exist"
        )
    # print(f"bot.api_key= {bot.api_key}")
    # print(f"bot.secret_key= {bot.secret_key}")
    bot.api_key = _services.fernet.encrypt(bot.api_key.encode()).decode()
    bot.secret_key = _services.fernet.encrypt(bot.secret_key.encode()).decode()
    # print(f"bot.api_key= {bot.api_key}")
    # print(f"bot.secret_key= {bot.secret_key}")
    return _services.create_bot(db=db, bot=bot, user_id=user_id)


@gridbotsRouter.get("/bots/", response_model=List[_schemas.Bot], tags=["Bot Methods"])
def read_bots(
    skip: int = 0,
    limit: int = 10,
    db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    bots = _services.get_bots(db=db, skip=skip, limit=limit)
    return bots


# @gridbotsRouter.get("/bots/{bot_id}", response_model=_schemas.Bot)
# def read_bot(bot_id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)):
#    bot = _services.get_bot(db=db, bot_id=bot_id)
#    if bot is None:
#        raise _fastapi.HTTPException(
#            status_code=404, detail="sorry this profit does not exist"
#        )
#    return bot


@gridbotsRouter.get(
    "/bots/{account}", response_model=_schemas.Bot, tags=["Bot Methods"]
)
def read_bot(account: str, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    bot = _services.get_bot(db=db, account=account)
    if bot is None:
        raise _fastapi.HTTPException(
            status_code=404, detail="sorry this profit does not exist"
        )
    return bot


@gridbotsRouter.delete("/bots/{bot_id}", tags=["Bot Methods"])
def delete_bot(bot_id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    _services.delete_bot(db=db, bot_id=bot_id)
    return {"message": f"successfully deleted bot with id: {bot_id}"}


@gridbotsRouter.put("/bots/{bot_id}", response_model=_schemas.Bot, tags=["Bot Methods"])
def update_bot(
    bot_id: int,
    bot: _schemas.BotCreate,
    db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    return _services.update_bot(db=db, bot=bot, bot_id=bot_id)


@gridbotsRouter.put(
    "/bots/update/{account}", response_model=_schemas.Bot, tags=["Bot Methods"]
)
def update_bot_by_account(
    account: str,
    bot: _schemas.BotCreate,
    db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    return _services.update_bot_by_account(db=db, bot=bot, account=account)
