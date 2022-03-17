"""init

Revision ID: 893ee680c780
Revises: 
Create Date: 2022-03-16 21:13:59.729398

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '893ee680c780'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('students',
        sa.Column('mssv', sa.Integer(), nullable=False),
        sa.Column('fullName', sa.String(length=100), nullable=False),
        sa.Column('classCode', sa.String(length=100), nullable=False),
        sa.PrimaryKeyConstraint('mssv')
    )

    op.create_table('positives',
        sa.Column('mssv', sa.Integer(), nullable=False),
        sa.Column('firstTestDay', sa.DateTime(), nullable=False),
        sa.Column('negativeDay', sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(['mssv'], ['students.mssv'], ),
        sa.PrimaryKeyConstraint('mssv')
    )



def downgrade():
    op.drop_table('positives')
    op.drop_table('students')
