import sqlalchemy.orm as _orm

import models as _models
import schemas as _schemas
import database as _database


def create_database():
    return _database.Base.metadata.create_all(bind=_database.engine)


def get_db():
    db = _database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_user(db: _orm.Session, user_id: int):
    return db.query(_models.User).filter(_models.User.id == user_id).first()


def get_user_by_email(db: _orm.Session, email: str):
    return db.query(_models.User).filter(_models.User.email == email).first()


def get_users(db: _orm.Session, skip: int = 0, limit: int = 100):
    return db.query(_models.User).offset(skip).limit(limit).all()


def create_user(db: _orm.Session, user: _schemas.UserCreate):
    fake_hashed_password = user.password + "thisisnotsecure"
    db_user = _models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# ------------------------------------------------------------------------


def get_bots(db: _orm.Session, skip: int = 0, limit: int = 10):
    return db.query(_models.Bot).offset(skip).limit(limit).all()


def create_bot(db: _orm.Session, bot: _schemas.BotCreate, user_id: int):
    bot = _models.Bot(**bot.dict(), owner_id=user_id)
    db.add(bot)
    db.commit()
    db.refresh(bot)
    return bot


def get_bot(db: _orm.Session, bot_id: int):
    return db.query(_models.Bot).filter(_models.Bot.id == bot_id).first()


def get_bot(db: _orm.Session, account: str):
    return db.query(_models.Bot).filter(_models.Bot.account == account).first()


def delete_bot(db: _orm.Session, bot_id: int):
    db.query(_models.Bot).filter(_models.Bot.id == bot_id).delete()
    db.commit()


def update_bot(db: _orm.Session, bot_id: int, bot: _schemas.BotCreate):
    db_bot = get_bot(db=db, bot_id=bot_id)
    db_bot.account = bot.account
    db_bot.symbol = bot.symbol
    db_bot.position_size = bot.position_size
    db_bot.grid_size = bot.grid_size
    db_bot.grid_mode = bot.grid_mode
    db_bot.follow_up = bot.follow_up
    db_bot.follow_down = bot.follow_down
    db_bot.num_buy_grid_lines = bot.num_buy_grid_lines
    db_bot.num_sell_grid_lines = bot.num_sell_grid_lines
    db_bot.check_orders_frequency = bot.check_orders_frequency
    db_bot.api_key = bot.api_key
    db_bot.secret_key = bot.secret_key
    db_bot.start_date = bot.start_date
    db_bot.start_price = bot.start_price

    db_bot.owner_id = bot.owner_id
    db.commit()
    db.refresh(db_bot)
    return db_bot


# ------------------------------------------------------------------------


def get_hourprofits(db: _orm.Session, skip: int = 0, limit: int = 10):
    return db.query(_models.HourProfit).offset(skip).limit(limit).all()


def create_hourprofit(
    db: _orm.Session, hourprofit: _schemas.HourProfitCreate, user_id: int
):
    hourprofit = _models.HourProfit(**hourprofit.dict(), owner_id=user_id)
    db.add(hourprofit)
    db.commit()
    db.refresh(hourprofit)
    return hourprofit


def get_hourprofit(db: _orm.Session, hourprofit_id: int):
    return (
        db.query(_models.HourProfit)
        .filter(_models.HourProfit.id == hourprofit_id)
        .first()
    )


def delete_hourprofit(db: _orm.Session, hourprofit_id: int):
    db.query(_models.HourProfit).filter(_models.HourProfit.id == hourprofit_id).delete()
    db.commit()


def update_hourprofit(
    db: _orm.Session, hourprofit_id: int, hourprofit: _schemas.HourProfitCreate
):
    db_hourprofit = get_hourprofit(db=db, hourprofit_id=hourprofit_id)
    db_hourprofit.account = hourprofit.account
    db_hourprofit.symbol = hourprofit.symbol
    db_hourprofit.balance_total = hourprofit.balance_total
    db_hourprofit.last_price = hourprofit.last_price
    db_hourprofit.coin_total = hourprofit.coin_total
    db_hourprofit.coin_free = hourprofit.coin_free
    db_hourprofit.coin_value = hourprofit.coin_value
    db_hourprofit.usd_total = hourprofit.usd_total
    db_hourprofit.usd_free = hourprofit.usd_free
    db_hourprofit.realized_hourprofit = hourprofit.realized_hourprofit
    db_hourprofit.unrealized_hourprofit = hourprofit.unrealized_hourprofit
    db_hourprofit.total_hourprofit = hourprofit.total_hourprofit
    db_hourprofit.investment = hourprofit.investment
    db_hourprofit.grid_apr = hourprofit.grid_apr
    db_hourprofit.duration = hourprofit.duration
    db_hourprofit.profit_per_grid = hourprofit.profit_per_grid
    db_hourprofit.mts_create = hourprofit.mts_create
    db_hourprofit.mts_update = hourprofit.mts_update
    db_hourprofit.owner_id = hourprofit.owner_id
    db.commit()
    db.refresh(db_hourprofit)
    return db_hourprofit


# ------------------------------------------------------------------------


def get_profits(db: _orm.Session, skip: int = 0, limit: int = 10):
    return db.query(_models.Profit).offset(skip).limit(limit).all()


def create_profit(db: _orm.Session, profit: _schemas.ProfitCreate, user_id: int):
    profit = _models.Profit(**profit.dict(), owner_id=user_id)
    db.add(profit)
    db.commit()
    db.refresh(profit)
    return profit


def get_profit(db: _orm.Session, profit_id: int):
    return db.query(_models.Profit).filter(_models.Profit.id == profit_id).first()


def delete_profit(db: _orm.Session, profit_id: int):
    db.query(_models.Profit).filter(_models.Profit.id == profit_id).delete()
    db.commit()


def update_profit(db: _orm.Session, profit_id: int, profit: _schemas.ProfitCreate):
    db_profit = get_profit(db=db, profit_id=profit_id)
    db_profit.account = profit.account
    db_profit.symbol = profit.symbol
    db_profit.balance_total = profit.balance_total
    db_profit.last_price = profit.last_price
    db_profit.coin_total = profit.coin_total
    db_profit.coin_free = profit.coin_free
    db_profit.coin_value = profit.coin_value
    db_profit.usd_total = profit.usd_total
    db_profit.usd_free = profit.usd_free
    db_profit.realized_profit = profit.realized_profit
    db_profit.unrealized_profit = profit.unrealized_profit
    db_profit.total_profit = profit.total_profit
    db_profit.investment = profit.investment
    db_profit.grid_apr = profit.grid_apr
    db_profit.duration = profit.duration
    db_profit.profit_per_grid = profit.profit_per_grid
    db_profit.mts_create = profit.mts_create
    db_profit.mts_update = profit.mts_update
    db_profit.owner_id = profit.owner_id
    db.commit()
    db.refresh(db_profit)
    return db_profit


# ------------------------------------------------------------------------
