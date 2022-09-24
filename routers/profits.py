from typing import List
import fastapi as _fastapi
import sqlalchemy.orm as _orm
import services as _services
import schemas as _schemas

profitsRouter = _fastapi.APIRouter()


@profitsRouter.post(
    "/bots/{bot_id}/profits/", response_model=_schemas.Profit, tags=["Profit Methods"]
)
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


@profitsRouter.get(
    "/profits/", response_model=List[_schemas.Profit], tags=["Profit Methods"]
)
def read_profits(
    skip: int = 0,
    limit: int = 10,
    db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    profits = _services.get_profits(db=db, skip=skip, limit=limit)
    return profits


@profitsRouter.get(
    "/profits/{profit_id}", response_model=_schemas.Profit, tags=["Profit Methods"]
)
def read_profit(profit_id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    profit = _services.get_profit(db=db, profit_id=profit_id)
    if profit is None:
        raise _fastapi.HTTPException(
            status_code=404, detail="sorry this profit does not exist"
        )

    return profit


@profitsRouter.delete("/profits/{profit_id}", tags=["Profit Methods"])
def delete_profit(
    profit_id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)
):
    _services.delete_profit(db=db, profit_id=profit_id)
    return {"message": f"successfully deleted profit with id: {profit_id}"}


@profitsRouter.put(
    "/profits/{profit_id}", response_model=_schemas.Profit, tags=["Profit Methods"]
)
def update_profit(
    profit_id: int,
    profit: _schemas.ProfitCreate,
    db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    return _services.update_profit(db=db, profit=profit, profit_id=profit_id)
