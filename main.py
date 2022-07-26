from typing import List
import fastapi as _fastapi
import sqlalchemy.orm as _orm
import services as _services
import schemas as _schemas

app = _fastapi.FastAPI()

_services.create_database()


@app.post("/users/", response_model=_schemas.User)
def create_user(
    user: _schemas.UserCreate, db: _orm.Session = _fastapi.Depends(_services.get_db)
):
    db_user = _services.get_user_by_email(db=db, email=user.email)
    if db_user:
        raise _fastapi.HTTPException(
            status_code=400, detail="woops the email is in use"
        )
    return _services.create_user(db=db, user=user)


@app.get("/users/", response_model=List[_schemas.User])
def read_users(
    skip: int = 0,
    limit: int = 10,
    db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    users = _services.get_users(db=db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=_schemas.User)
def read_user(user_id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    db_user = _services.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise _fastapi.HTTPException(
            status_code=404, detail="sorry this user does not exist"
        )
    return db_user


@app.post("/users/{user_id}/profits/", response_model=_schemas.Profit)
def create_profit(
    user_id: int,
    profit: _schemas.ProfitCreate,
    db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    db_user = _services.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise _fastapi.HTTPException(
            status_code=404, detail="sorry this user does not exist"
        )
    return _services.create_profit(db=db, profit=profit, user_id=user_id)


@app.get("/profits/", response_model=List[_schemas.Profit])
def read_profits(
    skip: int = 0,
    limit: int = 10,
    db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    profits = _services.get_profits(db=db, skip=skip, limit=limit)
    return profits


@app.get("/profits/{profit_id}", response_model=_schemas.Profit)
def read_profit(profit_id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    profit = _services.get_profit(db=db, profit_id=profit_id)
    if profit is None:
        raise _fastapi.HTTPException(
            status_code=404, detail="sorry this profit does not exist"
        )

    return profit


@app.delete("/profits/{profit_id}")
def delete_profit(profit_id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    _services.delete_profit(db=db, profit_id=profit_id)
    return {"message": f"successfully deleted post with id: {profit_id}"}


@app.put("/profits/{profit_id}", response_model=_schemas.Profit)
def update_post(
    profit_id: int,
    profit: _schemas.ProfitCreate,
    db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    return _services.update_post(db=db, profit=profit, profit_id=profit_id)
