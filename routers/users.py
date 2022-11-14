from typing import List
import fastapi as _fastapi
import sqlalchemy.orm as _orm
import services as _services
import schemas as _schemas

usersRouter = _fastapi.APIRouter()


@usersRouter.post("/users/", response_model=_schemas.User, tags=["User Methods"])
def create_user(
    user: _schemas.UserCreate, db: _orm.Session = _fastapi.Depends(_services.get_db)
):
    db_user = _services.get_user_by_email(db=db, email=user.email)
    if db_user:
        raise _fastapi.HTTPException(
            status_code=400, detail="woops the email is in use"
        )
    return _services.create_user(db=db, user=user)


@usersRouter.get("/users/", response_model=List[_schemas.User], tags=["User Methods"])
def read_users(
    skip: int = 0,
    limit: int = 10,
    db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    users = _services.get_users(db=db, skip=skip, limit=limit)
    return users


@usersRouter.get(
    "/users/{user_id}", response_model=_schemas.User, tags=["User Methods"]
)
def read_user(user_id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    db_user = _services.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise _fastapi.HTTPException(
            status_code=404, detail="sorry this user does not exist"
        )
    return db_user


# ------------------------------------------------
