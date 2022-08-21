import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm

from dotenv import load_dotenv
import os

# dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(".env")

### PostgreSQL ###
SQLALCHEMY_DATABASE_URL = os.environ.get("DATABASE_URL")

### MySQL ###
# SQLALCHEMY_DATABASE_URL = "mysql://root:iS27037888@localhost:3306/gridbot"

# MySQL engine = create_engine("mysql+pymysql://root@localhost:3306/test")
# pool_recycle=1 to solve the (2006, 'MySQL server has gone away') error
engine = _sql.create_engine(SQLALCHEMY_DATABASE_URL, pool_recycle=1)

### SQLite ###
# SQLALCHEMY_DATABASE_URL = "sqlite:///./database.db"
# SQLite should add `connect_args={"check_same_thread": False}`,
#   because SQLite only allow one thread to communicate with it
# engine = _sql.create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )

SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = _declarative.declarative_base()
