"""create active field for user types

Revision ID: 1d5b7ceedd97
Revises: cdbdbe658815
Create Date: 2021-02-10 18:51:22.879909

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1d5b7ceedd97'
down_revision = 'cdbdbe658815'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_types', sa.Column('active', sa.Integer(), nullable=False))
    user_types = sa.table('user_types',
                       sa.Column('id', sa.Integer),
                       sa.Column('name', sa.String),
                       sa.Column('active', sa.Integer)
                       )
    op.bulk_insert(user_types, [
        {'name': 'Klient', 'active': 1},
        {'name': 'Kontraktor', 'active': 1}
    ])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_types', 'active')
    # ### end Alembic commands ###
