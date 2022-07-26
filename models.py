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
    chat_id = _sql.Column(_sql.String(10))

    # profits = _orm.relationship("Profit", back_populates="owner")
    # hourprofits = _orm.relationship("HourProfit", back_populates="owner")
    bots = _orm.relationship("Bot", back_populates="owner")
    dcabots = _orm.relationship("DCABot", back_populates="owner")


class Bot(_database.Base):
    __tablename__ = "bots"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    owner_id = _sql.Column(
        _sql.Integer, _sql.ForeignKey("users.id")
    )  # TODO: change to user_id
    is_active = _sql.Column(_sql.Boolean, default=True)
    account = _sql.Column(_sql.String(50))
    symbol = _sql.Column(_sql.String(50))
    position_size = _sql.Column(_sql.Float, default=0)
    grid_size = _sql.Column(_sql.Float, default=0)
    cover_range = _sql.Column(_sql.Float, default=0)
    investment = _sql.Column(_sql.Float, default=0)
    start_price = _sql.Column(_sql.Float, default=0)
    start_date = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)
    follow_up = _sql.Column(_sql.Boolean, default=True)
    follow_down = _sql.Column(_sql.Boolean, default=False)
    grid_mode = _sql.Column(_sql.String(20))
    num_buy_grid_lines = _sql.Column(_sql.Integer, default=0)
    num_sell_grid_lines = _sql.Column(_sql.Integer, default=0)
    check_orders_frequency = _sql.Column(_sql.Integer, default=500)
    api_key = _sql.Column(_sql.String(140))
    secret_key = _sql.Column(_sql.String(140))
    date_created = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)
    date_last_updated = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)

    owner = _orm.relationship("User", back_populates="bots")

    profits = _orm.relationship("Profit", back_populates="robot")
    hourprofits = _orm.relationship("HourProfit", back_populates="robot")


class DCABot(_database.Base):
    __tablename__ = "dcabots"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    # owner_id = _sql.Column(_sql.Integer, _sql.ForeignKey("users.id"))
    user_id = _sql.Column(_sql.Integer, _sql.ForeignKey("users.id"))  # <----
    is_active = _sql.Column(_sql.Boolean, default=True)
    account = _sql.Column(_sql.String(50))
    sub_account = _sql.Column(_sql.String(50))
    symbol = _sql.Column(_sql.String(50))
    base_size = _sql.Column(_sql.Float, default=0)
    base_dollar = _sql.Column(_sql.Float, default=0)
    take_profit_pct = _sql.Column(_sql.Float, default=0)
    safety_pct = _sql.Column(_sql.Float, default=0)
    safety_dollar = _sql.Column(_sql.String(20), default=0)
    safety_size_multiplier = _sql.Column(_sql.String(20))
    safety_range_multiplier = _sql.Column(_sql.Integer, default=0)
    safety_range_start = _sql.Column(_sql.Integer, default=0)
    safety_max_times = _sql.Column(_sql.Integer, default=0)
    num_orders = _sql.Column(_sql.Integer, default=4)
    leverage = _sql.Column(_sql.Integer, default=20)
    position_mode = _sql.Column(_sql.String(7))
    start_mode = _sql.Column(_sql.String(30))
    trading_fee = _sql.Column(_sql.Float, default=0)
    use_existing_coin = _sql.Column(_sql.Boolean, default=False)
    paper_trading = _sql.Column(_sql.Boolean, default=False)
    dca_direction = _sql.Column(_sql.String(50))
    deal_wait_seconds = _sql.Column(_sql.Float, default=0)
    deal_drawdown_pct = _sql.Column(_sql.Float, default=0)
    stop_loss_pct = _sql.Column(_sql.Float, default=0)
    check_orders_frequency = _sql.Column(_sql.Float, default=0)
    platform = _sql.Column(_sql.String(12))
    supervisor = _sql.Column(_sql.String(20))
    sandbox = _sql.Column(_sql.Boolean, default=False)
    investment = _sql.Column(_sql.Float, default=0)
    start_price = _sql.Column(_sql.Float, default=0)
    start_date = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)

    api_key = _sql.Column(_sql.String(140))
    secret_key = _sql.Column(_sql.String(140))
    date_created = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)
    date_last_updated = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)

    owner = _orm.relationship("User", back_populates="dcabots")

    # dcatrans = _orm.relationship("DCATran", back_populates="robot")
    dcatrans = _orm.relationship("DCATran", back_populates="dcabot")


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
    date_created = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)
    date_last_updated = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)

    # owner_id = _sql.Column(_sql.Integer, _sql.ForeignKey("users.id"))
    # owner = _orm.relationship("User", back_populates="profits")
    robot_id = _sql.Column(_sql.Integer, _sql.ForeignKey("bots.id"))
    robot = _orm.relationship("Bot", back_populates="profits")


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
    date_created = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)
    date_last_updated = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)

    # owner_id = _sql.Column(_sql.Integer, _sql.ForeignKey("users.id"))
    # owner = _orm.relationship("User", back_populates="hourprofits")
    robot_id = _sql.Column(_sql.Integer, _sql.ForeignKey("bots.id"))
    robot = _orm.relationship("Bot", back_populates="hourprofits")


class DCATran(_database.Base):
    __tablename__ = "dcatrans"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    deal_id = _sql.Column(_sql.Integer, index=True)
    safety_times = _sql.Column(_sql.Integer, default=0)
    order_id = _sql.Column(_sql.String(36))
    side = _sql.Column(_sql.String(4))
    price = _sql.Column(_sql.Float, default=0)
    size = _sql.Column(_sql.Float, default=0)
    status = _sql.Column(_sql.String(8))
    profit = _sql.Column(_sql.Float, default=0)
    # date_created = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)
    # date_last_updated = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)
    date_created = _sql.Column(_sql.DateTime, default=_dt.datetime.now)
    date_last_updated = _sql.Column(_sql.DateTime, default=_dt.datetime.now)

    # owner_id = _sql.Column(_sql.Integer, _sql.ForeignKey("users.id"))
    # owner = _orm.relationship("User", back_populates="profits")
    dcabot_id = _sql.Column(_sql.Integer, _sql.ForeignKey("dcabots.id"))
    dcabot = _orm.relationship("DCABot", back_populates="dcatrans")
