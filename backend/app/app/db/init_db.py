from sqlalchemy.orm import Session

from app import crud, schemas
from app.core.config import settings
from app.db import base  # noqa: F401


# make sure all SQL Alchemy models are imported (app.db.base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28


def init_db(db: Session) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next line
    # Base.metadata.create_all(bind=engine)

    items = crud.item.get_multi(db)
    if not items:
        initial_items = [
            schemas.ItemCreate(
                title="This is my first task",
                checked=False
            ),
            schemas.ItemCreate(
                title="This is my already done task",
                checked=True
            ),
            schemas.ItemCreate(
                title="TODO: Add new task and check this as done",
                checked=False
            ),
            schemas.ItemCreate(
                title="Reload the page to see that tasks are stored in back-end database",
                checked=False
            ),
        ]
        for i in initial_items:
            crud.item.create(db, obj_in=i)

        print("Data initialisation completed.")
