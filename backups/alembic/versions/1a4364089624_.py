"""empty message

Revision ID: 1a4364089624
Revises: 
Create Date: 2023-05-10 17:36:39.319496

"""
from alembic import op
import sqlalchemy as sa


from database.migrations.tenant import for_each_tenant_schema

# revision identifiers, used by Alembic.
revision = '1a4364089624'
down_revision = None
branch_labels = None
depends_on = None


@for_each_tenant_schema
def upgrade(schema: str) -> None:
    preparer = sa.sql.compiler.IdentifierPreparer(op.get_bind().dialect)
    schema_quoted = preparer.format_schema(schema)




    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tenant',
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('schema', sa.String(), nullable=False),
    sa.Column('host', sa.String(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_by_id', sa.Integer(), nullable=True),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_by_id', sa.Integer(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.Column('tenant_id', sa.Integer(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('host'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('schema'),
    schema='shared'
    )
    op.create_table('bottle',
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_by_id', sa.Integer(), nullable=True),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_by_id', sa.Integer(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.Column('tenant_id', sa.Integer(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    schema='tenant_default'
    )
    op.create_table('item',
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_by_id', sa.Integer(), nullable=True),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_by_id', sa.Integer(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.Column('tenant_id', sa.Integer(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    schema='tenant_default'
    )
    op.create_table('product',
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_by_id', sa.Integer(), nullable=True),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_by_id', sa.Integer(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.Column('tenant_id', sa.Integer(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    schema='tenant_default'
    )
    # ### end Alembic commands ###


@for_each_tenant_schema
def downgrade(schema: str) -> None:
    preparer = sa.sql.compiler.IdentifierPreparer(op.get_bind().dialect)
    schema_quoted = preparer.format_schema(schema)

    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product', schema='tenant_default')
    op.drop_table('item', schema='tenant_default')
    op.drop_table('bottle', schema='tenant_default')
    op.drop_table('tenant', schema='shared')
    # ### end Alembic commands ###