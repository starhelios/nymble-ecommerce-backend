import uuid
from typing import Annotated

from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from src.modules.inventory.models import Inventory
from src.modules.order.models import Order
from src.modules.order.models import OrderItem
from src.modules.order.schema import CreateOrderDto
from src.modules.order.schema import CreateOrderItemDto
from src.modules.product.models import Product
from src.start.database import db_dependency


class OrderRepository:
    def __init__(self, db: db_dependency):
        self.db = db

    def get_orders(self):
        return self.db.query(Order).all()

    def get_order_items(self):
        return self.db.query(OrderItem).all()

    def create_order(self, create_order_dto: CreateOrderDto):
        order = Order(**create_order_dto.model_dump(), id=str(uuid.uuid4()))
        self.db.add(order)
        self.db.commit()
        self.db.refresh(order)
        return order

    def create_order_item(self, create_order_item_dto: CreateOrderItemDto):
        inventory = (
            self.db.query(Inventory)
            .filter_by(product_id=create_order_item_dto.product_id)
            .first()
        )
        if not inventory:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={"message": f"product not in stock"},
            )
        if inventory.stock < 1:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail={"message": "product not in stock"},
            )
        product = (
            self.db.query(Product)
            .filter_by(id=create_order_item_dto.product_id)
            .first()
        )
        inventory.stock = inventory.stock - 1
        order_item = OrderItem(
            **create_order_item_dto.model_dump(),
            id=str(uuid.uuid4()),
            price=product.price,
        )
        self.db.add(order_item)
        self.db.commit()
        self.db.refresh(order_item)
        return order_item


order_repository_dependency = Annotated[OrderRepository, Depends(OrderRepository)]
