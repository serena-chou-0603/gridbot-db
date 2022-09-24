from typing import List
import fastapi as _fastapi
import sqlalchemy.orm as _orm
import services as _services
import schemas as _schemas

hourprofitsRouter = _fastapi.APIRouter()


@hourprofitsRouter.post(
    "/bots/{bot_id}/hourprofits/",
    response_model=_schemas.HourProfit,
    tags=["HourProfit Methods"],
)
def create_hourprofit(
    bot_id: int,
    hourprofit: _schemas.ProfitCreate,
    db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    db_bot = _services.get_bot(db=db, bot_id=bot_id)
    if db_bot is None:
        raise _fastapi.HTTPException(
            status_code=404, detail="sorry this user does not exist"
        )
    return _services.create_hourprofit(db=db, hourprofit=hourprofit, bot_id=bot_id)


@hourprofitsRouter.get(
    "/hourprofits/",
    response_model=List[_schemas.HourProfit],
    tags=["HourProfit Methods"],
)
def read_hourprofits(
    skip: int = 0,
    limit: int = 10,
    db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    hourprofits = _services.get_hourprofits(db=db, skip=skip, limit=limit)
    return hourprofits


@hourprofitsRouter.get(
    "/hourprofits/{hourprofit_id}",
    response_model=_schemas.HourProfit,
    tags=["HourProfit Methods"],
)
def read_hourprofit(
    hourprofit_id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)
):
    hourprofit = _services.get_hourprofit(db=db, hourprofit_id=hourprofit_id)
    if hourprofit is None:
        raise _fastapi.HTTPException(
            status_code=404, detail="sorry this profit does not exist"
        )

    return hourprofit


@hourprofitsRouter.delete("/hourprofits/{hourprofit_id}", tags=["HourProfit Methods"])
def delete_hourprofit(
    hourprofit_id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)
):
    _services.delete_hourprofit(db=db, hourprofit_id=hourprofit_id)
    return {"message": f"successfully deleted hourprofit with id: {hourprofit_id}"}


@hourprofitsRouter.put(
    "/hourprofits/{hourprofit_id}",
    response_model=_schemas.HourProfit,
    tags=["HourProfit Methods"],
)
def update_hourprofit(
    hourprofit_id: int,
    hourprofit: _schemas.ProfitCreate,
    db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    return _services.update_hourprofit(
        db=db, hourprofit=hourprofit, hourprofit_id=hourprofit_id
    )
