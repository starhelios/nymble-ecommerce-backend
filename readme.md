# Configuring the database

First you'll need to go to terminal and run below commands in order to create a database
```shell
psql -U postgres
```

```sql
CREATE DATABASE ecommerce_app;
```

# Starting up the application

Make sure to create a .env file in root as per .env.example provided
Whenever you change .env (add or remove variables)
make sure to run following in terminal

```shell
source .env
```

Make sure pipenv is installed via python3
```shell
pip3 install pipenv

or

pip install pipenv
```

Create a virtual enviornment using command
```shell
pipenv shell
```

Install dependencies using command
```shell
pipenv install
```

You can open run.py in root & hit play button in your IDE to start the app as well.

Start the app using command
```shell
uvicorn src.main:app --reload
```

in production you can omit the reload flag and just use
command like this
```shell
uvicorn src.main:app
```

Optionally supply a port
```shell
uvicorn src.main:app --reload --port <port-number>
```

To auto generate migrations, run following command
```shell
alembic revision --autogenerate -m <migration-name>
 alembic revision --autogenerate -m "Schema Updates"
```

To run migrations and update database to most recent revision, run
```shell
alembic upgrade head
```
head points to most recent generated revision

To revert migrations, use following command
```shell
alembic downgrade -1
```

Details of alembic can be seen at link:
https://alembic.sqlalchemy.org/en/latest/tutorial.html

# Application api documentation

To view api documentation, visit <complete-host-url>/docs
example

http://127.0.0.1:8000/docs in case application is running locally

# Pre Commit Hooks

To run fixes, use following command:
```shell
pre-commit run --all-files
```
