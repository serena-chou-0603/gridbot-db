import datetime as _dt
from email.policy import default
import sqlalchemy as _sql
import sqlalchemy.orm as _orm

import database as _database


class User(_database.Base):
    __tablename__ = "users"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    email = _sql.Column(_sql.String(255), unique=True)
    hashed_password = _sql.Column(_sql.String(255))
    is_active = _sql.Column(_sql.Boolean, default=True)

    profits = _orm.relationship("Profit", back_populates="owner")
    hourprofits = _orm.relationship("HourProfit", back_populates="owner")
    bots = _orm.relationship("Bot", back_populates="owner")


class Bot(_database.Base):
    __tablename__ = "bots"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    account = _sql.Column(_sql.String(255))
    symbol = _sql.Column(_sql.String(255))
    position_size = _sql.Column(_sql.Float, default=0)
    grid_size = _sql.Column(_sql.Float, default=0)
    grid_mode = _sql.Column(_sql.String(20))
    follow_up = _sql.Column(_sql.Boolean, default=True)
    follow_down = _sql.Column(_sql.Boolean, default=False)
    num_buy_grid_lines = _sql.Column(_sql.Integer, default=0)
    num_sell_grid_lines = _sql.Column(_sql.Integer, default=0)
    check_orders_frequency = _sql.Column(_sql.Integer, default=500)
    investment = _sql.Column(_sql.Float, default=0)
    start_date = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)
    start_price = _sql.Column(_sql.Float, default=0)
    api_key = _sql.Column(_sql.String(40))
    secret_key = _sql.Column(_sql.String(40))

    owner_id = _sql.Column(_sql.Integer, _sql.ForeignKey("users.id"))
    date_created = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)
    date_last_updated = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)

    owner = _orm.relationship("User", back_populates="bots")


class Profit(_database.Base):
    __tablename__ = "profits"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    account = _sql.Column(_sql.String(255))
    symbol = _sql.Column(_sql.String(255))
    balance_total = _sql.Column(_sql.Float, default=0)
    last_price = _sql.Column(_sql.Float, default=0)
    coin_total = _sql.Column(_sql.Float, default=0)
    coin_free = _sql.Column(_sql.Float, default=0)
    coin_value = _sql.Column(_sql.Float, default=0)
    usd_total = _sql.Column(_sql.Float, default=0)
    usd_free = _sql.Column(_sql.Float, default=0)
    realized_profit = _sql.Column(_sql.Float, default=0)
    unrealized_profit = _sql.Column(_sql.Float, default=0)
    total_profit = _sql.Column(_sql.Float, default=0)
    investment = _sql.Column(_sql.Float, default=0)
    grid_apr = _sql.Column(_sql.Float, default=0)
    duration = _sql.Column(_sql.String(255))
    profit_per_grid = _sql.Column(_sql.Float, default=0)
    mts_create = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)
    mts_update = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)
    owner_id = _sql.Column(_sql.Integer, _sql.ForeignKey("users.id"))
    date_created = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)
    date_last_updated = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)

    owner = _orm.relationship("User", back_populates="profits")


class HourProfit(_database.Base):
    __tablename__ = "hourprofits"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    account = _sql.Column(_sql.String(255))
    symbol = _sql.Column(_sql.String(255))
    balance_total = _sql.Column(_sql.Float, default=0)
    last_price = _sql.Column(_sql.Float, default=0)
    coin_total = _sql.Column(_sql.Float, default=0)
    coin_free = _sql.Column(_sql.Float, default=0)
    coin_value = _sql.Column(_sql.Float, default=0)
    usd_total = _sql.Column(_sql.Float, default=0)
    usd_free = _sql.Column(_sql.Float, default=0)
    realized_profit = _sql.Column(_sql.Float, default=0)
    unrealized_profit = _sql.Column(_sql.Float, default=0)
    total_profit = _sql.Column(_sql.Float, default=0)
    investment = _sql.Column(_sql.Float, default=0)
    grid_apr = _sql.Column(_sql.Float, default=0)
    duration = _sql.Column(_sql.String(255))
    profit_per_grid = _sql.Column(_sql.Float, default=0)
    mts_create = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)
    mts_update = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)
    owner_id = _sql.Column(_sql.Integer, _sql.ForeignKey("users.id"))
    date_created = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)
    date_last_updated = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)

    owner = _orm.relationship("User", back_populates="hourprofits")
