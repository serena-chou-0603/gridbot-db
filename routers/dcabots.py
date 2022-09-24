from typing import List
import fastapi as _fastapi
import sqlalchemy.orm as _orm
import services as _services
import schemas as _schemas

dcabotsRouter = _fastapi.APIRouter()


@dcabotsRouter.post(
    "/users/{user_id}/dcabots/", response_model=_schemas.DCABot, tags=["DCABot Methods"]
)
def create_dcabot(
    user_id: int,
    dcabot: _schemas.DCABotCreate,
    db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    db_user = _services.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise _fastapi.HTTPException(
            status_code=404, detail="sorry this user does not exist"
        )
    # print(f"bot.api_key= {bot.api_key}")
    # print(f"bot.secret_key= {bot.secret_key}")
    dcabot.api_key = _services.fernet.encrypt(dcabot.api_key.encode()).decode()
    dcabot.secret_key = _services.fernet.encrypt(dcabot.secret_key.encode()).decode()
    # print(f"bot.api_key= {bot.api_key}")
    # print(f"bot.secret_key= {bot.secret_key}")
    return _services.create_dcabot(db=db, dcabot=dcabot, user_id=user_id)


@dcabotsRouter.get(
    "/dcabots/", response_model=List[_schemas.DCABot], tags=["DCABot Methods"]
)
def read_dcabots(
    skip: int = 0,
    limit: int = 10,
    db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    dcabots = _services.get_dcabots(db=db, skip=skip, limit=limit)
    return dcabots


# @dcabotsRouter.get("/dcabots/{bot_id}", response_model=_schemas.DCABot)
# def read_dcabot(bot_id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)):
#    dcabot = _services.get_dcabot(db=db, dcabot_id=dcabot_id)
#    if dcabot is None:
#        raise _fastapi.HTTPException(
#            status_code=404, detail="sorry this profit does not exist"
#        )
#    return dcabot


@dcabotsRouter.get(
    "/dcabots/{account}", response_model=_schemas.DCABot, tags=["DCABot Methods"]
)
def read_bot(account: str, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    dcabot = _services.get_dcabot(db=db, account=account)
    if dcabot is None:
        raise _fastapi.HTTPException(
            status_code=404, detail="sorry this profit does not exist"
        )
    return dcabot


@dcabotsRouter.delete("/dcabots/{bot_id}", tags=["DCABot Methods"])
def delete_dcabot(
    dcabot_id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)
):
    _services.delete_dcabot(db=db, dcabot_id=dcabot_id)
    return {"message": f"successfully deleted bot with id: {dcabot_id}"}


@dcabotsRouter.put(
    "/dcabots/{dcabot_id}", response_model=_schemas.DCABot, tags=["DCABot Methods"]
)
def update_dcabot(
    dcabot_id: int,
    dcabot: _schemas.BotCreate,
    db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    return _services.update_dcabot(db=db, dcabot=dcabot, dcabot_id=dcabot_id)


@dcabotsRouter.put(
    "/dcabots/update/{account}", response_model=_schemas.DCABot, tags=["DCABot Methods"]
)
def update_dcabot_by_account(
    account: str,
    dcabot: _schemas.DCABotCreate,
    db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    return _services.update_dcabot_by_account(db=db, dcabot=dcabot, account=account)
