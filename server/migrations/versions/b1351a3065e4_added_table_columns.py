"""added table columns

Revision ID: b1351a3065e4
Revises: a50cde241c4b
Create Date: 2023-10-09 00:20:46.108513

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b1351a3065e4'
down_revision = 'a50cde241c4b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('baked_goods', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('price', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True))
        batch_op.add_column(sa.Column('updated_at', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('bakery_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_baked_goods_bakery_id_bakeries'), 'bakeries', ['bakery_id'], ['id'])
    with op.batch_alter_table('bakeries', schema=None) as batch_op:   
        batch_op.add_column(sa.Column('name', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True))
        batch_op.add_column(sa.Column('updated_at', sa.DateTime(), nullable=True))


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('bakeries', 'updated_at')
    op.drop_column('bakeries', 'created_at')
    op.drop_column('bakeries', 'name')
    op.drop_constraint(op.f('fk_baked_goods_bakery_id_bakeries'), 'baked_goods', type_='foreignkey')
    op.drop_column('baked_goods', 'bakery_id')
    op.drop_column('baked_goods', 'updated_at')
    op.drop_column('baked_goods', 'created_at')
    op.drop_column('baked_goods', 'price')
    op.drop_column('baked_goods', 'name')
    # ### end Alembic commands ###
