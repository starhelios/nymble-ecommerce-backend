from typing import Annotated

from fastapi import Depends

from src.modules.order.repository import order_repository_dependency
from src.modules.order.schema import CreateOrderDto
from src.modules.order.schema import CreateOrderItemDto


class OrderService:
    def __init__(self, order_repository: order_repository_dependency):
        self.order_repository = order_repository

    def get_orders(self):
        return self.order_repository.get_orders()

    def get_order_items(self):
        return self.order_repository.get_order_items()

    def create_order(self, create_order_dto: CreateOrderDto):
        return self.order_repository.create_order(create_order_dto)

    def create_order_item(self, create_order_item_dto: CreateOrderItemDto):
        return self.order_repository.create_order_item(create_order_item_dto)


order_service_dependency = Annotated[OrderService, Depends(OrderService)]
