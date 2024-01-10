from fastapi import APIRouter

from src.modules.order.schema import CreateOrderDto
from src.modules.order.schema import CreateOrderItemDto
from src.modules.order.schema import OrderItemResponse
from src.modules.order.schema import OrderResponse
from src.modules.order.service import order_service_dependency

orders = APIRouter(prefix="/api/orders", tags=["orders"])


@orders.get("/", response_model=list[OrderResponse])
def get_orders(order_service: order_service_dependency):
    return order_service.get_orders()


@orders.get("/order-item", response_model=list[OrderItemResponse])
def get_order_items(order_service: order_service_dependency):
    return order_service.get_order_items()


@orders.post("/", response_model=OrderResponse)
def create_order(
    order_service: order_service_dependency,
    create_order_dto: CreateOrderDto,
):
    return order_service.create_order(create_order_dto)


@orders.post("/order-item", response_model=OrderItemResponse)
def create_order_item(
    order_service: order_service_dependency, create_order_item_dto: CreateOrderItemDto
):
    return order_service.create_order_item(create_order_item_dto)
