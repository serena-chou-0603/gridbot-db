### install

```
$ git clone https://github.com/serena-chou-0603/gridbot-db.git
$ cd gridbot-db
$ chmod +x bootstrap.sh
$ docker build .
```

#### install for dev environment

- change docker-compose.yml to use `command: bash -c "/app/bootstrap.sh" # debug mode`

```
$ docker-compose up -d
```

#### install for production environment

- change docker-compose.yml to use `command: bash -c "uvicorn main:app --host 0.0.0.0 --port 8000 --reload" # production mode`

```
$ docker-compose up -d
```

### create database from phpmyadmin

```
visit https://gridbot.ezcoin.cc/pdm/, create database `gridbot`

$ docker exec -it app /bin/bash
:/app# uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### gridbot-db

Youtube:
https://www.youtube.com/watch?v=NH4VZaP3_9s&t=14s&ab_channel=VeryAcademy

```
$ python -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
```

### db

FastAPI with SQL (ORM) - https://www.youtube.com/watch?v=eltKL8kC160

```
(.venv) $ cd db
(.venv) $ uvicorn main:app --reload
(.venv) $ uvicorn main:app --host 0.0.0.0 --reload
```

### db operation

```
$ mysql -u root -p
mysql> drop DATABASE gridbot;
mysql> create database `gridbot` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
```

```
scp database.py tokyo_01:/home/ubuntu/python/gridbot-db/
scp main.py tokyo_01:/home/ubuntu/python/gridbot-db/
scp models.py tokyo_01:/home/ubuntu/python/gridbot-db/
scp schemas.py tokyo_01:/home/ubuntu/python/gridbot-db/
scp services.py tokyo_01:/home/ubuntu/python/gridbot-db/
scp -r routers/ tokyo_01:/home/ubuntu/python/gridbot-db/
```
