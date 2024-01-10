from typing import Annotated

from fastapi import Depends
from sqlalchemy import text

from src.modules.admin.schema import StatsResponse
from src.start.database import db_dependency


class AdminRepository:
    def __init__(self, db: db_dependency):
        self.db = db

    def get_stats(self) -> StatsResponse:
        query = text(
            """
            SELECT
                COALESCE(SUM(CASE WHEN EXTRACT(YEAR FROM o.created_at) = EXTRACT(YEAR FROM CURRENT_DATE) THEN oi.price ELSE 0 END), 0) AS total_sales_current_year,
                COALESCE(SUM(CASE WHEN EXTRACT(YEAR FROM o.created_at) = EXTRACT(YEAR FROM CURRENT_DATE) - 1 THEN oi.price ELSE 0 END), 0) AS total_sales_previous_year,
                COUNT(DISTINCT CASE WHEN EXTRACT(YEAR FROM u.created_at) = EXTRACT(YEAR FROM CURRENT_DATE) THEN u.id END) AS new_customers_current_year,
                COUNT(DISTINCT CASE WHEN EXTRACT(YEAR FROM u.created_at) = EXTRACT(YEAR FROM CURRENT_DATE) - 1 THEN u.id END) AS new_customers_previous_year,
                COUNT(CASE WHEN f.rating BETWEEN 1 AND 2 THEN f.id END) AS negative_feedbacks,
                COUNT(CASE WHEN f.rating = 3 THEN f.id END) AS neutral_feedbacks,
                COUNT(CASE WHEN f.rating BETWEEN 4 AND 5 THEN f.id END) AS positive_feedbacks
            FROM
                orders o
            JOIN
                order_items oi ON o.id = oi.order_id
            JOIN
                users u ON o.customer_id = u.id
            LEFT JOIN
                feedbacks f ON oi.product_id = f.product_id
        """
        )
        result = self.db.execute(query)
        rows = result.fetchall()
        return [
            dict(
                zip(
                    (
                        "total_sales_current_year",
                        "total_sales_previous_year",
                        "new_customers_current_year",
                        "new_customers_previous_year",
                        "negative_feedbacks",
                        "neutral_feedbacks",
                        "positive_feedbacks",
                    ),
                    row,
                )
            )
            for row in rows
        ][0]


admin_repository_dependency = Annotated[AdminRepository, Depends(AdminRepository)]
