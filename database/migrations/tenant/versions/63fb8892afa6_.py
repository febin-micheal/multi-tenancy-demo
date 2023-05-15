"""empty message

Revision ID: 63fb8892afa6
Revises: 
Create Date: 2023-05-11 15:30:23.465312

"""
from alembic import op
import sqlalchemy as sa


from database.migrations.tenant import for_each_tenant_schema

# revision identifiers, used by Alembic.
revision = '63fb8892afa6'
down_revision = None
branch_labels = None
depends_on = None


@for_each_tenant_schema
def upgrade(schema: str) -> None:
    preparer = sa.sql.compiler.IdentifierPreparer(op.get_bind().dialect)
    schema_quoted = preparer.format_schema(schema)

    # ### commands auto generated by Alembic - please adjust! ###
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
    schema=schema_quoted
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
    schema=schema_quoted
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
    schema=schema_quoted
    )
    # ### end Alembic commands ###


@for_each_tenant_schema
def downgrade(schema: str) -> None:
    preparer = sa.sql.compiler.IdentifierPreparer(op.get_bind().dialect)
    schema_quoted = preparer.format_schema(schema)

    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product', schema=schema_quoted)
    op.drop_table('item', schema=schema_quoted)
    op.drop_table('bottle', schema=schema_quoted)
    # ### end Alembic commands ###
