"""fix table cars model and rental cars models

Revision ID: 6f77b4bcd892
Revises: 
Create Date: 2022-03-03 09:52:56.763882

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6f77b4bcd892'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tb_cars',
    sa.Column('chassi', sa.String(), nullable=False),
    sa.Column('license_plate', sa.String(), nullable=False),
    sa.Column('brand', sa.String(), nullable=False),
    sa.Column('model', sa.String(), nullable=False),
    sa.Column('year', sa.String(), nullable=False),
    sa.Column('color_car', sa.String(), nullable=False),
    sa.Column('image', sa.String(), nullable=False),
    sa.Column('current_km', sa.Float(), nullable=False),
    sa.Column('licensing_expiration', sa.DateTime(), nullable=False),
    sa.Column('daily_rental_price', sa.Float(), nullable=False),
    sa.Column('daily_fixed_km', sa.Integer(), nullable=False),
    sa.Column('available', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('chassi'),
    sa.UniqueConstraint('license_plate')
    )
    op.create_table('tb_users',
    sa.Column('cnh', sa.String(length=11), nullable=False),
    sa.Column('cpf', sa.String(length=11), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('phone', sa.String(length=11), nullable=False),
    sa.Column('categorie_cnh', sa.String(length=2), nullable=False),
    sa.PrimaryKeyConstraint('cnh'),
    sa.UniqueConstraint('cpf'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phone')
    )
    op.create_table('tb_rental_cars',
    sa.Column('rental_id', sa.Integer(), nullable=False),
    sa.Column('rental_date', sa.DateTime(), nullable=False),
    sa.Column('rental_return_date', sa.DateTime(), nullable=False),
    sa.Column('rental_real_return_date', sa.DateTime(), nullable=True),
    sa.Column('returned_car', sa.Boolean(), nullable=True),
    sa.Column('rental_total_days', sa.Integer(), nullable=False),
    sa.Column('rental_real_total_days', sa.Integer(), nullable=False),
    sa.Column('initial_km', sa.Float(), nullable=False),
    sa.Column('final_km', sa.Float(), nullable=False),
    sa.Column('total_fixed_km', sa.Integer(), nullable=False),
    sa.Column('total_returned_km', sa.Float(), nullable=True),
    sa.Column('rental_value', sa.Float(), nullable=False),
    sa.Column('rental_real_value', sa.Float(), nullable=True),
    sa.Column('customer_cnh', sa.String(), nullable=False),
    sa.Column('car_license_plate', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['car_license_plate'], ['tb_cars.license_plate'], ),
    sa.ForeignKeyConstraint(['customer_cnh'], ['tb_users.cnh'], ),
    sa.PrimaryKeyConstraint('rental_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tb_rental_cars')
    op.drop_table('tb_users')
    op.drop_table('tb_cars')
    # ### end Alembic commands ###
