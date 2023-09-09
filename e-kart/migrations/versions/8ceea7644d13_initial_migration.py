"""Initial migration.

Revision ID: 8ceea7644d13
Revises: 
Create Date: 2023-06-20 14:50:14.584746

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "8ceea7644d13"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "category",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("category", sa.String(length=255), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("category"),
    )
    op.create_table(
        "sizes",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("size", sa.String(length=5), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "user",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_name", sa.String(length=255), nullable=True),
        sa.Column("email", sa.String(length=255), nullable=True),
        sa.Column("password", sa.String(length=255), nullable=True),
        sa.Column("first_name", sa.String(length=255), nullable=True),
        sa.Column("last_name", sa.String(length=255), nullable=True),
        sa.Column("date_of_join", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )
    op.create_table(
        "ekart",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("category_id", sa.Integer(), nullable=False),
        sa.Column("gender", sa.Enum("MALE", "FEMALE", name="gender"), nullable=True),
        sa.Column("product_code", sa.String(length=255), nullable=False),
        sa.Column("product_name", sa.String(length=255), nullable=True),
        sa.Column("available_quantity", sa.Integer(), nullable=True),
        sa.Column("size_id", sa.Integer(), nullable=False),
        sa.Column("price", sa.Float(), nullable=True),
        sa.Column("created", sa.DateTime(), nullable=True),
        sa.Column("updated", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(["category_id"], ["category.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["size_id"], ["sizes.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("product_code"),
    )
    op.create_table(
        "cart_items",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("cart_item", sa.Integer(), nullable=False),
        sa.Column("quantity", sa.Integer(), nullable=True),
        sa.Column("added_datetime", sa.DateTime(), nullable=True),
        sa.Column("updated", sa.DateTime(), nullable=True),
        sa.Column("total_price", sa.Float(), nullable=True),
        sa.Column("user", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["cart_item"], ["ekart.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["user"], ["user.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "wish_list",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("cart_item", sa.Integer(), nullable=False),
        sa.Column("added_datetime", sa.DateTime(), nullable=True),
        sa.Column("user", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["cart_item"], ["ekart.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["user"], ["user.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("cart_item"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("wish_list")
    op.drop_table("cart_items")
    op.drop_table("ekart")
    op.drop_table("user")
    op.drop_table("sizes")
    op.drop_table("category")
    # ### end Alembic commands ###
