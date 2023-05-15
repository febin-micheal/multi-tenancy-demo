from typing import Optional

import uvicorn

import alembic

import sqlalchemy as sa
from pydantic.dataclasses import contextmanager
from sqlalchemy.orm import Session

from alembic import command
from alembic.config import Config
from alembic.runtime.migration import MigrationContext
from fastapi import FastAPI, Depends, Request
from sqlalchemy import MetaData, select, inspect
from starlette_admin.contrib.sqla import Admin

from project.database import engine
from tenants import TENANT_LIST
from tests import schemas
from tests.models import Tenant

from tests.routers import router as tests_router
from utils.base import Base


# Base.metadata.create_all(bind=engine)


def get_shared_metadata():
    meta = MetaData()
    for table in Base.metadata.tables.values():
        if table.schema != "tenant":
            table.to_metadata(meta)
    return meta


# alembic_config = Config("//alembic.ini")


def shared_create() -> None:
    with engine.begin() as db:
        # context = MigrationContext.configure(db)
        # if context.get_current_revision() is not None:
        #     print("Database already exists.")
        #     return

        db.execute(sa.schema.CreateSchema("shared"))
        # get_shared_metadata().create_all(bind=db)

        # alembic_config.attributes["connection"] = db
        # command.stamp(alembic_config, "head", purge=True)
        #


@contextmanager
def with_db(tenant_schema: Optional[str]):
    if tenant_schema:
        schema_translate_map = dict(tenant=tenant_schema)
    else:
        schema_translate_map = None

    connectable = engine.execution_options(schema_translate_map=schema_translate_map)

    db = Session(autocommit=False, autoflush=False, bind=connectable)
    try:
        yield db
    finally:
        db.close()


def get_tenant_specific_metadata():
    meta = MetaData(schema="tenant")
    for table in Base.metadata.tables.values():
        if table.schema == "tenant":
            table.to_metadata(meta)
    return meta


def tenant_create(name: str, schema: str, host: str) -> None:
    with with_db(schema) as db:
        # context = MigrationContext.configure(db.connection())
        # script = alembic.script.ScriptDirectory.from_config(alembic_config)
        # if context.get_current_revision() != script.get_current_head():
        #     raise RuntimeError(
        #         "Database is not up-to-date. Execute migrations before adding new tenants."
        #     )

        inspector = inspect(engine)

        if schema in inspector.get_schema_names():
            print("hi hello", schema)
            pass
        else:
            # tenant = Tenant(
            #     name=name,
            #     host=host,
            #     schema=schema,
            # )
            # db.add(tenant)

            db.execute(sa.schema.CreateSchema(schema))
        # get_tenant_specific_metadata().create_all(bind=db.connection())

        db.commit()


class TenantNotFoundError(Exception):
    pass


def get_tenant(req: Request) -> Tenant:
    host_without_port = req.headers["host"]
    # host_without_port = req.headers["host"].split(":", 1)[0]
    print(host_without_port)

    with with_db(None) as db:
        tenant = db.query(Tenant).filter(Tenant.host == host_without_port).one_or_none()

    if tenant is None:
        raise TenantNotFoundError()

    return tenant


def get_db(tenant: Tenant = Depends(get_tenant)):
    with with_db(tenant.schema) as db:
        yield db


app = FastAPI()
# app = FastAPI(openapi_url="/api/openapi.json", docs_url="/api/docs")


@app.get("/")
def root(request: Request):
    return {"Host": request.headers["host"]}


@app.get("/tenant", response_model=None)
# @app.get("/tenant", response_model=schemas.TenantInfo)
def get_tenant(db: Session = Depends(get_db), tenant: Tenant = Depends(get_tenant)):
    # Do something with db
    return tenant


@app.post("/tenant", response_model=None)
# @app.get("/tenant", response_model=schemas.TenantInfo)
def create_tenant(db: Session = Depends(get_db), tenant: Tenant = Depends(get_tenant)):
    # Do something with db
    return tenant


# Create admin
admin = Admin(engine, title="Multi Tenancy Demo")

# # Add view
from tests.admin import *

# Mount admin to your app
admin.mount_to(app)


@app.get("/api/")
async def root():
    return {"message": "Welcome to Multi Tenancy Demo"}


# Include app-wise routers below
app.include_router(router=tests_router)


if __name__ == "__main__":
    # print("Hello World")
    inspector = inspect(engine)

    if "shared" in inspector.get_schema_names():
        print("Shared already exists")
    else:
        shared_create()
        print("Shared created")

    for tenant in TENANT_LIST:
        # print(tenant["name"])
        tenant_create(name=tenant["name"], schema=tenant["schema"], host=tenant["host"])

    # uvicorn.run(app)
