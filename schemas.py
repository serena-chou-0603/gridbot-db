from typing import List
import datetime as _dt
import pydantic as _pydantic


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
class _PostBase(_pydantic.BaseModel):
    title: str
    content: str


class PostCreate(_PostBase):
    pass


class Post(_PostBase):
    # {
    #     "id": 1,
    #     "owner_id": 23,
    #     "title": "this is a title",
    #     "content": "some content for the post",
    #     "date_created": "12-12-12 00:00:00"
    #     "date_last_update": "12-12-12 00:00:00"
    # }
    id: int
    owner_id: int
    date_created: _dt.datetime
    date_last_updated: _dt.datetime

    # default orm_mode = Fasle
    class Config:
        orm_mode = True


class _UserBase(_pydantic.BaseModel):
    email: str


class UserCreate(_UserBase):
    password: str


class User(_UserBase):
    id: int
    is_active: bool
    posts: List[Post] = []

    class Config:
        orm_mode = True
