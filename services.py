from sqlalchemy import and_
import sqlalchemy.orm as _orm
import models as _models
import schemas as _schemas
import database as _database
from cryptography.fernet import Fernet
import os

fernet = Fernet(os.environ.get("FERNET_KEY").encode())


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


def get_dcabots(db: _orm.Session, skip: int = 0, limit: int = 10):
    # return db.query(_models.Bot).offset(skip).limit(limit).all()
    # select only is_active bots
    return (
        db.query(_models.DCABot)
        .filter(_models.DCABot.is_active == True)
        .offset(skip)
        .limit(limit)
        .all()
    )


def create_dcabot(db: _orm.Session, dcabot: _schemas.DCABotCreate, user_id: int):
    dcabot = _models.DCABot(**dcabot.dict(), user_id=user_id)
    db.add(dcabot)
    db.commit()
    db.refresh(dcabot)
    return dcabot


# def get_bot(db: _orm.Session, bot_id: int):
#    return db.query(_models.Bot).filter(_models.Bot.id == bot_id).first()
#
# def get_bot(db: _orm.Session, account: str):
#    return db.query(_models.Bot).filter(_models.Bot.account == account).first()
def get_dcabot(db: _orm.Session, dcabot_id: int = -1, account: str = ""):
    if dcabot_id > 0:
        return (
            db.query(_models.DCABot)
            .filter(
                and_(_models.DCABot.id == dcabot_id, _models.DCABot.is_active == True)
            )
            .first()
        )
    if account != "":
        return (
            db.query(_models.DCABot)
            .filter(
                and_(
                    _models.DCABot.account == account, _models.DCABot.is_active == True
                )
            )
            .first()
        )


def delete_dcabot(db: _orm.Session, dcabot_id: int):
    db.query(_models.DCABot).filter(_models.DCABot.id == dcabot_id).delete()
    db.commit()


def update_dcabot(db: _orm.Session, dcabot_id: int, dcabot: _schemas.DCABotCreate):
    db_dcabot = get_bot(db=db, dcabot_id=dcabot_id)
    db_dcabot.account = dcabot.account
    db_dcabot.sub_account = dcabot.sub_account
    db_dcabot.symbol = dcabot.symbol
    db_dcabot.base_size = dcabot.base_size
    db_dcabot.base_dollar = dcabot.base_dollar
    db_dcabot.take_profit_pct = dcabot.take_profit_pct
    db_dcabot.safety_pct = dcabot.safety_pct
    db_dcabot.safety_size_multiplier = dcabot.safety_size_multiplier
    db_dcabot.safety_range_multiplier = dcabot.safety_range_multiplier
    db_dcabot.start_mode = dcabot.start_mode
    db_dcabot.trading_fee = dcabot.trading_fee
    db_dcabot.use_existing_coin = dcabot.use_existing_coin
    db_dcabot.paper_trading = dcabot.paper_trading
    db_dcabot.dca_direction = dcabot.dca_direction
    db_dcabot.deal_wait_seconds = dcabot.deal_wait_seconds
    db_dcabot.check_orders_frequency = dcabot.check_orders_frequency
    db_dcabot.investment = dcabot.investment
    db_dcabot.api_key = dcabot.api_key
    db_dcabot.secret_key = dcabot.secret_key
    db_dcabot.start_date = dcabot.start_date
    db_dcabot.start_price = dcabot.start_price
    db_dcabot.user_id = dcabot.user_id
    db.commit()
    db.refresh(db_dcabot)
    return db_dcabot


def update_dcabot_by_account(
    db: _orm.Session, account: str, dcabot: _schemas.DCABotCreate
):
    db_dcabot = get_dcabot(db=db, account=account)
    # print(f"services.py, update_bot_by_account(), bot= {bot}")
    # print("db_bot.id= ", db_bot.id)
    # print("bot.cover_range= ", bot.cover_range)
    db_dcabot.sub_account = (
        dcabot.sub_account if dcabot.sub_account is not None else db_dcabot.sub_account
    )
    db_dcabot.symbol = dcabot.symbol if dcabot.symbol is not None else db_dcabot.symbol
    db_dcabot.base_size = (
        dcabot.base_size if dcabot.base_size is not None else db_dcabot.base_size
    )
    db_dcabot.base_dollar = (
        dcabot.base_dollar if dcabot.base_dollar is not None else db_dcabot.base_dollar
    )
    db_dcabot.take_profit_pct = (
        dcabot.take_profit_pct
        if dcabot.take_profit_pct is not None
        else db_dcabot.take_profit_pct
    )
    db_dcabot.safety_pct = (
        dcabot.safety_pct if dcabot.safety_pct is not None else db_dcabot.safety_pct
    )
    db_dcabot.safety_size_multiplier = (
        dcabot.safety_size_multiplier
        if dcabot.safety_size_multiplier is not None
        else db_dcabot.safety_size_multiplier
    )
    db_dcabot.safety_range_multiplier = (
        dcabot.safety_range_multiplier
        if dcabot.safety_range_multiplier is not None
        else db_dcabot.safety_range_multiplier
    )
    db_dcabot.start_mode = (
        dcabot.start_mode if dcabot.start_mode is not None else db_dcabot.start_mode
    )
    db_dcabot.trading_fee = (
        dcabot.trading_fee if dcabot.trading_fee is not None else db_dcabot.trading_fee
    )
    db_dcabot.use_existing_coin = (
        dcabot.use_existing_coin
        if dcabot.use_existing_coin is not None
        else db_dcabot.use_existing_coin
    )
    db_dcabot.paper_trading = (
        dcabot.paper_trading
        if dcabot.paper_trading is not None
        else db_dcabot.paper_trading
    )
    db_dcabot.check_orders_frequency = (
        dcabot.check_orders_frequency
        if dcabot.check_orders_frequency is not None
        else db_dcabot.check_orders_frequency
    )
    db_dcabot.investment = (
        dcabot.investment if dcabot.investment is not None else db_dcabot.investment
    )
    db_dcabot.api_key = (
        dcabot.api_key if dcabot.api_key is not None else db_dcabot.api_key
    )
    db_dcabot.secret_key = (
        dcabot.secret_key if dcabot.secret_key is not None else db_dcabot.secret_key
    )
    db_dcabot.start_date = (
        dcabot.start_date if dcabot.start_date is not None else db_dcabot.start_date
    )
    db_dcabot.start_price = (
        dcabot.start_price if dcabot.start_price is not None else db_dcabot.start_price
    )
    db.commit()
    db.refresh(db_dcabot)
    return db_dcabot


# ------------------------------------------------------------------------


def get_bots(db: _orm.Session, skip: int = 0, limit: int = 10):
    # return db.query(_models.Bot).offset(skip).limit(limit).all()
    # select only is_active bots
    return (
        db.query(_models.Bot)
        .filter(_models.Bot.is_active == True)
        .offset(skip)
        .limit(limit)
        .all()
    )


def create_bot(db: _orm.Session, bot: _schemas.BotCreate, user_id: int):
    bot = _models.Bot(**bot.dict(), owner_id=user_id)
    db.add(bot)
    db.commit()
    db.refresh(bot)
    return bot


# def get_bot(db: _orm.Session, bot_id: int):
#    return db.query(_models.Bot).filter(_models.Bot.id == bot_id).first()
#
# def get_bot(db: _orm.Session, account: str):
#    return db.query(_models.Bot).filter(_models.Bot.account == account).first()
def get_bot(db: _orm.Session, bot_id: int = -1, account: str = ""):
    if bot_id > 0:
        return (
            db.query(_models.Bot)
            .filter(and_(_models.Bot.id == bot_id, _models.Bot.is_active == True))
            .first()
        )
    if account != "":
        return (
            db.query(_models.Bot)
            .filter(and_(_models.Bot.account == account, _models.Bot.is_active == True))
            .first()
        )


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


def update_bot_by_account(db: _orm.Session, account: str, bot: _schemas.BotCreate):
    db_bot = get_bot(db=db, account=account)
    # print(f"services.py, update_bot_by_account(), bot= {bot}")
    # print("db_bot.id= ", db_bot.id)
    # print("bot.cover_range= ", bot.cover_range)
    if bot.cover_range is not None:
        db_bot.cover_range = bot.cover_range
    db.commit()
    db.refresh(db_bot)
    return db_bot


# ------------------------------------------------------------------------


def get_hourprofits(db: _orm.Session, skip: int = 0, limit: int = 10):
    return db.query(_models.HourProfit).offset(skip).limit(limit).all()


def create_hourprofit(
    db: _orm.Session, hourprofit: _schemas.HourProfitCreate, bot_id: int
):
    hourprofit = _models.HourProfit(**hourprofit.dict(), robot_id=bot_id)
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
    db_hourprofit.realized_profit = hourprofit.realized_profit
    db_hourprofit.unrealized_profit = hourprofit.unrealized_profit
    db_hourprofit.total_profit = hourprofit.total_profit
    db_hourprofit.investment = hourprofit.investment
    db_hourprofit.grid_apr = hourprofit.grid_apr
    db_hourprofit.duration = hourprofit.duration
    db_hourprofit.profit_per_grid = hourprofit.profit_per_grid
    db_hourprofit.mts_create = hourprofit.mts_create
    db_hourprofit.mts_update = hourprofit.mts_update
    # db_hourprofit.robot_id = hourprofit.robot_id
    db.commit()
    db.refresh(db_hourprofit)
    return db_hourprofit


# ------------------------------------------------------------------------


def get_profits(db: _orm.Session, skip: int = 0, limit: int = 10):
    return db.query(_models.Profit).offset(skip).limit(limit).all()


def create_profit(db: _orm.Session, profit: _schemas.ProfitCreate, bot_id: int):
    profit = _models.Profit(**profit.dict(), robot_id=bot_id)
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
    # db_profit.robot_id = profit.robot_id
    db.commit()
    db.refresh(db_profit)
    return db_profit


# ------------------------------------------------------------------------
# ------------------------------------------------------------------------


def get_dcatrans(db: _orm.Session, skip: int = 0, limit: int = 10):
    # return db.query(_models.Bot).offset(skip).limit(limit).all()
    # select only is_active bots
    return (
        db.query(_models.DCATran)
        # .filter(_models.DCATran.is_active == True)
        .offset(skip)
        .limit(limit)
        .all()
    )


def create_dcatran(db: _orm.Session, dcatran: _schemas.DCATranCreate, dcabot_id: int):
    dcatran = _models.DCATran(**dcatran.dict(), dcabot_id=dcabot_id)
    db.add(dcatran)
    db.commit()
    db.refresh(dcatran)
    return dcatran


def get_dcatran_orderid(db: _orm.Session, dcabot_id: int, order_id: int):
    if dcabot_id > 0:
        return (
            db.query(_models.DCATran)
            .filter(
                and_(
                    _models.DCATran.dcabot_id == dcabot_id,
                    _models.DCATran.order_id == order_id,
                )
            )
            .order_by(_models.DCATran.id.desc())
            .first()
        )


# def get_bot(db: _orm.Session, bot_id: int):
#    return db.query(_models.Bot).filter(_models.Bot.id == bot_id).first()
#
# def get_bot(db: _orm.Session, account: str):
#    return db.query(_models.Bot).filter(_models.Bot.account == account).first()
def get_dcatran(db: _orm.Session, dcatran_id: int = -1, account: str = ""):
    if dcatran_id > 0:
        return (
            db.query(_models.DCATran)
            .filter(and_(_models.DCATran.id == dcatran_id))
            .first()
        )
    if account != "":
        return (
            db.query(_models.DCATran)
            .filter(
                and_(
                    _models.DCATran.account == account,
                    _models.DCATran.is_active == True,
                )
            )
            .first()
        )


def delete_dcatran(db: _orm.Session, dcatran_id: int):
    db.query(_models.DCATran).filter(_models.DCATran.id == dcatran_id).delete()
    db.commit()


def update_dcatran(db: _orm.Session, dcatran_id: int, dcatran: _schemas.DCATranCreate):
    db_dcatran = get_dcatran(db=db, dcatran_id=dcatran_id)
    db_dcatran.deal_id = dcatran.deal_id
    db_dcatran.safety_times = dcatran.safety_times
    db_dcatran.side = dcatran.side
    db_dcatran.price = dcatran.price
    db_dcatran.status = dcatran.status
    db_dcatran.profit = dcatran.profit
    db_dcatran.date_created = dcatran.date_created
    db_dcatran.date_last_updated = dcatran.date_last_updated
    db_dcatran.dcabot_id = dcatran.dcabot_id
    db.commit()
    db.refresh(db_dcatran)
    return db_dcatran


def update_dcatran_by_account(
    db: _orm.Session, account: str, dcatran: _schemas.DCATranCreate
):
    db_dcatran = get_dcatran(db=db, account=account)
    # print(f"services.py, update_bot_by_account(), bot= {bot}")
    # print("db_bot.id= ", db_bot.id)
    # print("bot.cover_range= ", bot.cover_range)
    if dcatran.cover_range is not None:
        db_dcatran.cover_range = dcatran.cover_range
    db.commit()
    db.refresh(db_dcatran)
    return db_dcatran


# ------------------------------------------------------------------------
