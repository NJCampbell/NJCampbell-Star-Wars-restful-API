"""empty message

Revision ID: fd1d12fd2a5d
Revises: 8903aab22d34
Create Date: 2023-09-13 19:04:09.713097

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fd1d12fd2a5d'
down_revision = '8903aab22d34'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('diameter', sa.String(length=250), nullable=True),
    sa.Column('rotation_period', sa.String(length=250), nullable=True),
    sa.Column('orbital_period', sa.String(length=250), nullable=True),
    sa.Column('population', sa.String(length=250), nullable=True),
    sa.Column('climate', sa.String(length=250), nullable=True),
    sa.Column('terrain', sa.String(length=250), nullable=True),
    sa.Column('description', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('vehicles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('model', sa.String(length=250), nullable=False),
    sa.Column('vehicle_class', sa.String(length=250), nullable=True),
    sa.Column('manufacturer', sa.String(length=250), nullable=True),
    sa.Column('cost_in_credits', sa.String(length=250), nullable=True),
    sa.Column('length', sa.String(length=250), nullable=True),
    sa.Column('crew', sa.String(length=250), nullable=True),
    sa.Column('passengers', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('people',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('height', sa.String(length=250), nullable=True),
    sa.Column('mass', sa.String(length=250), nullable=True),
    sa.Column('hair_color', sa.String(length=250), nullable=True),
    sa.Column('skin_color', sa.String(length=250), nullable=True),
    sa.Column('eye_color', sa.String(length=250), nullable=True),
    sa.Column('gender', sa.String(length=250), nullable=True),
    sa.Column('description', sa.String(length=250), nullable=True),
    sa.Column('planet_id', sa.Integer(), nullable=True),
    sa.Column('vehicle_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['planet_id'], ['planets.id'], ),
    sa.ForeignKeyConstraint(['vehicle_id'], ['vehicles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favorites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('person_id', sa.Integer(), nullable=True),
    sa.Column('planet_id', sa.Integer(), nullable=True),
    sa.Column('vehicle_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['person_id'], ['people.id'], ),
    sa.ForeignKeyConstraint(['planet_id'], ['planets.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['vehicle_id'], ['vehicles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favorites')
    op.drop_table('people')
    op.drop_table('vehicles')
    op.drop_table('planets')
    # ### end Alembic commands ###
