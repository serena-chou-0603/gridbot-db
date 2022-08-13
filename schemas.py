from typing import List
import datetime as _dt
import pydantic as _pydantic


class _BotBase(_pydantic.BaseModel):
    account: str
    symbol: str
    position_size: float
    grid_size: float
    grid_mode: str
    follow_up: bool
    follow_down: bool
    num_buy_grid_lines: int
    num_sell_grid_lines: int
    check_orders_frequency: int
    api_key: str
    secret_key: str
    investment: float
    start_date: _dt.datetime
    start_price: float
    # ERROR date_created: _dt.datetime
    # ERROR date_last_updated: _dt.datetime


class BotCreate(_BotBase):
    pass


class Bot(_BotBase):
    id: int
    owner_id: int
    date_created: _dt.datetime
    date_last_updated: _dt.datetime

    # default orm_mode = Fasle
    class Config:
        orm_mode = True


# -----------------------------------------------


class _ProfitBase(_pydantic.BaseModel):
    account: str
    symbol: str
    balance_total: float
    last_price: float
    coin_total: float
    coin_free: float
    coin_value: float
    usd_total: float
    usd_free: float
    realized_profit: float
    unrealized_profit: float
    total_profit: float
    investment: float
    grid_apr: float
    duration: str
    profit_per_grid: float
    mts_create: _dt.datetime
    mts_update: _dt.datetime
    # ERROR date_created: _dt.datetime
    # ERROR date_last_updated: _dt.datetime


class ProfitCreate(_ProfitBase):
    pass


class Profit(_ProfitBase):
    id: int
    owner_id: int
    date_created: _dt.datetime
    date_last_updated: _dt.datetime

    # default orm_mode = Fasle
    class Config:
        orm_mode = True


# -----------------------------------------------


class HourProfitCreate(_ProfitBase):
    pass


class HourProfit(_ProfitBase):
    id: int
    owner_id: int
    date_created: _dt.datetime
    date_last_updated: _dt.datetime

    # default orm_mode = Fasle
    class Config:
        orm_mode = True


# -----------------------------------------------


class _UserBase(_pydantic.BaseModel):
    email: str


class UserCreate(_UserBase):
    password: str


class User(_UserBase):
    id: int
    is_active: bool
    profits: List[Profit] = []

    class Config:
        orm_mode = True
