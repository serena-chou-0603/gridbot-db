### install

```
$ git clone ...
$ cd gridbot-db
$ chmod +x bootstrap.sh
$ docker build .
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
scp database.py dchou2006_1:/home/ubuntu/gridbit-db/
scp main.py dchou2006_1:/home/ubuntu/gridbot-db/
scp models.py dchou2006_1:/home/ubuntu/gridbot-db/
scp schemas.py dchou2006_1:/home/ubuntu/gridbot-db/
scp services.py dchou2006_1:/home/ubuntu/gridbot-db/
```
