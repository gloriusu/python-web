"""empty message

Revision ID: f818b25aa254
Revises: b9a3b98aee93
Create Date: 2021-11-19 19:42:12.323084

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f818b25aa254'
down_revision = 'b9a3b98aee93'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('about_me', sa.Text(), nullable=True))
        batch_op.drop_column('test_field')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('test_field', sa.VARCHAR(length=20), nullable=True))
        batch_op.drop_column('about_me')

    # ### end Alembic commands ###
