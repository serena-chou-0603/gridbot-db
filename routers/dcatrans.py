from typing import List
import fastapi as _fastapi
import sqlalchemy.orm as _orm
import services as _services
import schemas as _schemas

dcatransRouter = _fastapi.APIRouter()


@dcatransRouter.post(
    "/dcabots/{dcabot_id}/dcatrans/",
    response_model=_schemas.DCATran,
    tags=["DCATran Methods"],
)
def create_dcatran(
    dcabot_id: int,
    dcatran: _schemas.DCATranCreate,
    db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    db_dcabot = _services.get_dcabot(db=db, dcabot_id=dcabot_id)
    if db_dcabot is None:
        raise _fastapi.HTTPException(
            status_code=404, detail="sorry this dcabot does not exist"
        )
    return _services.create_dcatran(db=db, dcatran=dcatran, dcabot_id=dcabot_id)


@dcatransRouter.post(
    "/dcabots/{dcabot_id}/order/{order_id}",
    response_model=_schemas.DCATran,
    tags=["DCATran Methods"],
)
def create_or_update_dcatran(
    dcabot_id: int,
    order_id: int,
    # NG dcatran: _schemas.DCATranCreate,
    dcatran: _schemas.DCATran,  # OK because `update`, need to change DCATranCreate to DCATran
    db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    # find order_id
    db_dcatran = _services.get_dcatran_orderid(
        db=db, dcabot_id=dcabot_id, order_id=order_id
    )
    if db_dcatran is None:
        # create
        db_dcabot = _services.get_dcabot(db=db, dcabot_id=dcabot_id)
        if db_dcabot is None:
            raise _fastapi.HTTPException(
                status_code=404, detail="sorry this dcabot does not exist"
            )
        return _services.create_dcatran(db=db, dcatran=dcatran, dcabot_id=dcabot_id)
    else:
        # update
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


@dcatransRouter.get(
    "/dcabots/{dcabot_id}/order/{order_id}",
    response_model=_schemas.DCATran,
    tags=["DCATran Methods"],
)
def get_dcatran_orderid(
    dcabot_id: int,
    order_id: int,
    db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    db_dcatran = _services.get_dcatran_orderid(
        db=db, dcabot_id=dcabot_id, order_id=order_id
    )
    if db_dcatran is None:
        raise _fastapi.HTTPException(
            status_code=404, detail="sorry this dcabot does not exist"
        )
    return db_dcatran


@dcatransRouter.get(
    "/dcatrans/",
    response_model=List[_schemas.DCATran],
    tags=["DCATran Methods"],
)
def read_dcatrans(
    skip: int = 0,
    limit: int = 10,
    db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    dcatrans = _services.get_dcatrans(db=db, skip=skip, limit=limit)
    return dcatrans


@dcatransRouter.get(
    "/dcatrans/{dcatran_id}",
    response_model=_schemas.DCATran,
    tags=["DCATran Methods"],
)
def read_dcatran(
    dcatran_id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)
):
    dcatran = _services.get_dcatran(db=db, dcatran_id=dcatran_id)
    if dcatran is None:
        raise _fastapi.HTTPException(
            status_code=404, detail="sorry this dcatran does not exist"
        )

    return dcatran


@dcatransRouter.delete("/dcatrans/{dcatran_id}", tags=["DCATran Methods"])
def delete_dcatran(
    dcatran_id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)
):
    _services.delete_dcatran(db=db, dcatran_id=dcatran_id)
    return {"message": f"successfully deleted dcatran with id: {dcatran_id}"}


@dcatransRouter.put(
    "/dcatrans/{dcatran_id}",
    response_model=_schemas.DCATran,
    tags=["DCATran Methods"],
)
def update_dcatran(
    dcatran_id: int,
    dcatran: _schemas.DCATran,
    db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    return _services.update_dcatran(db=db, dcatran=dcatran, dcatran_id=dcatran_id)
