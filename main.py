from typing import List
import fastapi as _fastapi
import sqlalchemy.orm as _orm
import services as _services
import schemas as _schemas

app = _fastapi.FastAPI()

_services.create_database()


@app.post("/users/", response_model=_schemas.User)
def create_user(
    user: _schemas.UserCreate, db: _orm.Session = _fastapi.Depends(_services.get_db)
):
    db_user = _services.get_user_by_email(db=db, email=user.email)
    if db_user:
        raise _fastapi.HTTPException(
            status_code=400, detail="woops the email is in use"
        )
    return _services.create_user(db=db, user=user)


@app.get("/users/", response_model=List[_schemas.User])
def read_users(
    skip: int = 0,
    limit: int = 10,
    db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    users = _services.get_users(db=db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=_schemas.User)
def read_user(user_id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    db_user = _services.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise _fastapi.HTTPException(
            status_code=404, detail="sorry this user does not exist"
        )
    return db_user


# ------------------------------------------------


@app.post("/users/{user_id}/bots/", response_model=_schemas.Bot)
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
    return _services.create_bot(db=db, bot=bot, user_id=user_id)


@app.get("/bots/", response_model=List[_schemas.Bot])
def read_bots(
    skip: int = 0,
    limit: int = 10,
    db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    bots = _services.get_bots(db=db, skip=skip, limit=limit)
    return bots


# @app.get("/bots/{bot_id}", response_model=_schemas.Bot)
# def read_bot(bot_id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)):
#    bot = _services.get_bot(db=db, bot_id=bot_id)
#    if bot is None:
#        raise _fastapi.HTTPException(
#            status_code=404, detail="sorry this profit does not exist"
#        )
#
#    return bot


@app.get("/bots/{account}", response_model=_schemas.Bot)
def read_bot(account: str, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    bot = _services.get_bot(db=db, account=account)
    if bot is None:
        raise _fastapi.HTTPException(
            status_code=404, detail="sorry this profit does not exist"
        )

    return bot


@app.delete("/bots/{bot_id}")
def delete_bot(bot_id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    _services.delete_bot(db=db, profit_id=bot_id)
    return {"message": f"successfully deleted bot with id: {bot_id}"}


@app.put("/bots/{bot_id}", response_model=_schemas.Bot)
def update_bot(
    bot_id: int,
    bot: _schemas.ProfitCreate,
    db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    return _services.update_bot(db=db, bot=bot, bot_id=bot_id)


# ------------------------------------------------


@app.post("/bots/{bot_id}/profits/", response_model=_schemas.Profit)
def create_profit(
    bot_id: int,
    profit: _schemas.ProfitCreate,
    db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    print(f"create_profit(), bot_id= {bot_id}")
    db_bot = _services.get_bot(db=db, bot_id=bot_id)
    if db_bot is None:
        raise _fastapi.HTTPException(
            status_code=404, detail="sorry this bot does not exist"
        )
    return _services.create_profit(db=db, profit=profit, bot_id=bot_id)


@app.get("/profits/", response_model=List[_schemas.Profit])
def read_profits(
    skip: int = 0,
    limit: int = 10,
    db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    profits = _services.get_profits(db=db, skip=skip, limit=limit)
    return profits


@app.get("/profits/{profit_id}", response_model=_schemas.Profit)
def read_profit(profit_id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    profit = _services.get_profit(db=db, profit_id=profit_id)
    if profit is None:
        raise _fastapi.HTTPException(
            status_code=404, detail="sorry this profit does not exist"
        )

    return profit


@app.delete("/profits/{profit_id}")
def delete_profit(
    profit_id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)
):
    _services.delete_profit(db=db, profit_id=profit_id)
    return {"message": f"successfully deleted profit with id: {profit_id}"}


@app.put("/profits/{profit_id}", response_model=_schemas.Profit)
def update_profit(
    profit_id: int,
    profit: _schemas.ProfitCreate,
    db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    return _services.update_profit(db=db, profit=profit, profit_id=profit_id)


# ------------------------------------------------


@app.post("/bots/{bot_id}/hourprofits/", response_model=_schemas.HourProfit)
def create_hourprofit(
    bot_id: int,
    hourprofit: _schemas.ProfitCreate,
    db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    db_bot = _services.get_bot(db=db, bot_id=bot_id)
    if db_bot is None:
        raise _fastapi.HTTPException(
            status_code=404, detail="sorry this user does not exist"
        )
    return _services.create_hourprofit(db=db, hourprofit=hourprofit, bot_id=bot_id)


@app.get("/hourprofits/", response_model=List[_schemas.HourProfit])
def read_hourprofits(
    skip: int = 0,
    limit: int = 10,
    db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    hourprofits = _services.get_hourprofits(db=db, skip=skip, limit=limit)
    return hourprofits


@app.get("/hourprofits/{hourprofit_id}", response_model=_schemas.HourProfit)
def read_hourprofit(
    hourprofit_id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)
):
    hourprofit = _services.get_hourprofit(db=db, hourprofit_id=hourprofit_id)
    if hourprofit is None:
        raise _fastapi.HTTPException(
            status_code=404, detail="sorry this profit does not exist"
        )

    return hourprofit


@app.delete("/hourprofits/{hourprofit_id}")
def delete_hourprofit(
    hourprofit_id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)
):
    _services.delete_hourprofit(db=db, hourprofit_id=hourprofit_id)
    return {"message": f"successfully deleted hourprofit with id: {hourprofit_id}"}


@app.put("/hourprofits/{hourprofit_id}", response_model=_schemas.HourProfit)
def update_hourprofit(
    hourprofit_id: int,
    hourprofit: _schemas.ProfitCreate,
    db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    return _services.update_hourprofit(
        db=db, hourprofit=hourprofit, hourprofit_id=hourprofit_id
    )
