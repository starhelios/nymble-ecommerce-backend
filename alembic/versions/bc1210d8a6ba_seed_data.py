"""Seed data

Revision ID: bc1210d8a6ba
Revises: 155131564b80
Create Date: 2024-01-05 23:50:50.751935

"""
import uuid
from typing import Sequence
from typing import Union

import requests
import sqlalchemy as sa
from faker import Faker
from sqlalchemy.orm import Session

from alembic import op
from src.modules.feedback.models import Feedback
from src.modules.inventory.models import Inventory
from src.modules.order.models import Order
from src.modules.order.models import OrderItem
from src.modules.product.models import Product
from src.modules.user.models import User

# revision identifiers, used by Alembic.
revision: str = "bc1210d8a6ba"
down_revision: Union[str, None] = "155131564b80"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

fake = Faker()


def generate_uuid():
    return str(uuid.uuid4())


def seed_data(db: Session):
    # Seed Users
    for _ in range(10):
        db.add(
            User(
                id=generate_uuid(),
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.email(),
                password=fake.password(),
            )
        )

    # Seed Products
    response = requests.get("https://fakestoreapi.com/products?limit=100")
    products_data = response.json()
    for product_data in products_data:
        db.add(
            Product(
                id=generate_uuid(),
                title=product_data["title"],
                description=product_data["description"],
                image=product_data["image"],
                price=float(product_data["price"]),
            )
        )

    db.commit()

    # Seed Feedbacks, Inventories, Orders, and OrderItems
    users = db.query(User).all()
    products = db.query(Product).all()

    for product in products:
        user = fake.random_element(users)

        # Seed Feedbacks
        db.add(
            Feedback(
                id=generate_uuid(),
                customer_id=user.id,
                product_id=product.id,
                rating=fake.random_int(min=1, max=5),
                comment=fake.text(),
            )
        )

        # Seed Inventories (check for existing record before insertion)
        existing_inventory = (
            db.query(Inventory).filter_by(product_id=product.id).first()
        )
        if not existing_inventory:
            db.add(
                Inventory(
                    id=generate_uuid(),
                    product_id=product.id,
                    stock=fake.random_int(min=0, max=10000),
                )
            )

        # Seed Orders
        db.add(Order(id=generate_uuid(), customer_id=user.id))

    orders = db.query(Order).all()

    for order in orders:
        product = fake.random_element(products)
        # Seed OrderItems
        db.add(
            OrderItem(
                id=generate_uuid(),
                order_id=order.id,
                product_id=product.id,
                quantity=fake.random_int(min=1, max=10),
                price=product.price,
            )
        )

    db.commit()


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###

    # Seed data after migrating
    engine = op.get_bind()
    Session = sa.orm.sessionmaker(bind=engine)

    with Session() as session:
        seed_data(session)


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
