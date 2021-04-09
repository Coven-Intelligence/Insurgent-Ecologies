"""new user columns

Revision ID: afaed769139d
Revises: 3d69fc945ee3
Create Date: 2021-03-30 11:04:12.870224

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'afaed769139d'
down_revision = '3d69fc945ee3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('magickal_interventions', schema=None) as batch_op:
        batch_op.drop_index('ix_magickal_interventions_spell_timestamp')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('magickal_interventions', schema=None) as batch_op:
        batch_op.create_index('ix_magickal_interventions_spell_timestamp', ['spell_timestamp'], unique=False)

    # ### end Alembic commands ###
