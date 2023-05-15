import functools
from typing import Callable

from sqlalchemy import text, inspect
from sqlalchemy.orm import sessionmaker
from typeguard import typechecked
from alembic import op
from project.database import engine


@typechecked
def for_each_tenant_schema(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapped():
        # Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        # session = Session()
        # stmt = text("SELECT schema FROM shared.tenant")
        # # stmt = text("SELECT schema FROM shared.tenants")
        # schemas = session.execute(stmt).fetchall()
        # # print(schemas)

        # stmt = text("SELECT schema FROM shared.tenants")
        # schemas = op.get_bind().execute(text).fetchall()
        # schemas = op.get_bind().execute("SELECT schema FROM shared.tenant").fetchall()

        # for (schema,) in schemas:
        #     print(schema)
        #     func(schema)

        inspector = inspect(engine)
        schemas = inspector.get_schema_names()
        print(schemas)
        schemas.remove("shared")
        schemas.remove("public")
        schemas.remove("information_schema")

        print(type(schemas))
        print(schemas)

        for schema in schemas:
            print(schema)
            print(type(schema))
            func(schema)

    return wrapped
