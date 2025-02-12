"""empty message

Revision ID: 880dbfb66b87
Revises: 2f69a6a058e1
Create Date: 2023-09-13 19:24:24.357843

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '880dbfb66b87'
down_revision = '2f69a6a058e1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('vehicles', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description', sa.String(length=250), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('vehicles', schema=None) as batch_op:
        batch_op.drop_column('description')

    # ### end Alembic commands ###
