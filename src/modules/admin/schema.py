from pydantic import BaseModel


class StatsResponse(BaseModel):
    total_sales_current_year: float
    total_sales_previous_year: float
    new_customers_current_year: int
    new_customers_previous_year: int
    negative_feedbacks: int
    neutral_feedbacks: int
    positive_feedbacks: int
