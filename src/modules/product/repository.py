import uuid
from datetime import datetime
from datetime import timedelta
from typing import Annotated

from fastapi import Depends
from sqlalchemy import func
from sqlalchemy import text

from src.modules.order.models import Order
from src.modules.order.models import OrderItem
from src.modules.product.models import Product
from src.modules.product.schema import CreateProductDto
from src.start.database import db_dependency


class ProductRepository:
    def __init__(self, db: db_dependency) -> None:
        self.db = db

    def get_products(self):
        return self.db.query(Product).all()

    def get_top_selling(self):
        query = text(
            """
            SELECT
                p.*,
                SUM(oi.quantity) AS total_sold
            FROM order_items oi
            JOIN products p ON oi.product_id = p.id
            GROUP BY p.id
            ORDER BY total_sold DESC
            LIMIT 5
        """
        )
        result = self.db.execute(query)
        rows = result.fetchall()
        result_dict = [
            {
                "title": row[0],
                "description": row[1],
                "image": row[2],
                "price": row[3],
                "id": row[4],
                "created_at": row[5].isoformat(),
                "updated_at": row[6].isoformat(),
                "total_sold": row[7],
            }
            for row in rows
        ]
        return result_dict

    def create_product(self, create_product_dto: CreateProductDto):
        product = Product(**create_product_dto.model_dump(), id=str(uuid.uuid4()))
        self.db.add(product)
        self.db.commit()
        self.db.refresh(product)
        return product

    def get_product_sales(self, product_id: str):
        current_date = datetime.now()
        end_of_previous_month = current_date.replace(day=1) - timedelta(days=1)
        start_of_previous_month = end_of_previous_month.replace(day=1)

        start_of_current_month = current_date.replace(day=1)

        previous_month_sales = (
            self.db.query(func.sum(OrderItem.quantity).label("total_quantity"))
            .join(Order)
            .filter(
                OrderItem.product_id == product_id,
                Order.created_at >= start_of_previous_month,
                Order.created_at <= end_of_previous_month,
            )
            .group_by(OrderItem.product_id)
            .first()
        )

        current_month_sales = (
            self.db.query(func.sum(OrderItem.quantity).label("total_quantity"))
            .join(Order)
            .filter(
                OrderItem.product_id == product_id,
                Order.created_at >= start_of_current_month,
            )
            .group_by(OrderItem.product_id)
            .first()
        )

        sales_data = {
            "product_id": product_id,
            "previous_month_sales": previous_month_sales.total_quantity
            if previous_month_sales
            else 0,
            "current_month_sales": current_month_sales.total_quantity
            if current_month_sales
            else 0,
        }

        return sales_data


product_repository_dependency = Annotated[ProductRepository, Depends(ProductRepository)]
