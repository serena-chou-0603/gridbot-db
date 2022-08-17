from typing import List
import datetime as _dt
import pydantic as _pydantic
from typing import Optional


class _BotBase(_pydantic.BaseModel):
    account: str
    is_active: Optional[bool] = None
    symbol: Optional[str] = None
    position_size: Optional[float] = None
    grid_size: Optional[float] = None
    cover_range: Optional[float] = None
    grid_mode: Optional[str] = None
    follow_up: Optional[bool] = None
    follow_down: Optional[bool] = None
    num_buy_grid_lines: Optional[int] = None
    num_sell_grid_lines: Optional[int] = None
    check_orders_frequency: Optional[int] = None
    api_key: Optional[str] = None
    secret_key: Optional[str] = None
    investment: Optional[float] = None
    start_date: Optional[_dt.datetime] = None
    start_price: Optional[float] = None
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
    robot_id: int
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
    robot_id: int
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
