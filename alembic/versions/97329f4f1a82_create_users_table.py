"""Create users table

Revision ID: 97329f4f1a82
Revises: 
Create Date: 2020-11-04 13:11:34.297311

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '97329f4f1a82'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op. create_table(
        "user",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("username", sa.String),
        sa.Column("password", sa.String)
    )


def downgrade():
    op.drop_table("user")
