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
    db_user = _models.User(
        email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_profits(db: _orm.Session, skip: int = 0, limit: int = 10):
    return db.query(_models.Profit).offset(skip).limit(limit).all()


def create_profit(db: _orm.Session, profit: _schemas.ProfitCreate, user_id: int):
    profit = _models.Profit(**profit.dict(), owner_id=user_id)
    db.add(profit)
    db.commit()
    db.refresh(profit)
    return profit

# ------------------------------------------------------------------------


def get_profit(db: _orm.Session, profit_id: int):
    return db.query(_models.Profit).filter(_models.Profit.id == profit_id).first()


def delete_profit(db: _orm.Session, profit_id: int):
    db.query(_models.Profit).filter(_models.Profit.id == profit_id).delete()
    db.commit()


def update_post(db: _orm.Session, profit_id: int, profit: _schemas.PostCreate):
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
