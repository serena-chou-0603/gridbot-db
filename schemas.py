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


class _DCABotBase(_pydantic.BaseModel):
    account: str
    sub_account: str
    is_active: Optional[bool] = None
    symbol: Optional[str] = None
    base_size: Optional[float] = None
    base_dollar: Optional[float] = None
    take_profit_pct: Optional[float] = None
    safety_pct: Optional[float] = None
    safety_dollar: Optional[float] = None
    safety_size_multiplier: Optional[float] = None
    safety_range_multiplier: Optional[float] = None
    safety_max_times: Optional[int] = None
    num_orders: Optional[int] = None
    start_mode: Optional[str] = None
    trading_fee: Optional[float] = None
    use_existing_coin: Optional[bool] = None
    paper_trading: Optional[bool] = None
    dca_direction: Optional[str] = None
    deal_wait_seconds: Optional[float] = None
    check_orders_frequency: Optional[float] = None
    platform: Optional[str] = None
    supervisor: Optional[str] = None

    investment: Optional[float] = None
    start_price: Optional[float] = None
    start_date: Optional[float] = None

    api_key: Optional[str] = None
    secret_key: Optional[str] = None

    start_date: Optional[_dt.datetime] = None
    start_price: Optional[float] = None
    # ERROR date_created: _dt.datetime
    # ERROR date_last_updated: _dt.datetime


class DCABotCreate(_DCABotBase):
    pass


class DCABot(_DCABotBase):
    id: int
    user_id: int
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
    password: Optional[str] = None
    chat_id: Optional[str] = None


class User(_UserBase):
    id: int
    is_active: bool
    chat_id: str
    profits: List[Profit] = []

    class Config:
        orm_mode = True


# -----------------------------------------------


class _DCATranBase(_pydantic.BaseModel):
    deal_id: Optional[int] = None
    safety_times: Optional[int] = None
    order_id: Optional[str] = None
    side: Optional[str] = None
    price: Optional[float] = None
    size: Optional[float] = None
    status: Optional[str] = None
    profit: Optional[float] = None
    # ERROR date_created: _dt.datetime
    # ERROR date_last_updated: _dt.datetime


class DCATranCreate(_DCATranBase):
    pass


class DCATran(_DCATranBase):
    id: int
    dcabot_id: int
    date_created: _dt.datetime
    date_last_updated: _dt.datetime

    # default orm_mode = Fasle
    class Config:
        orm_mode = True


# -----------------------------------------------
