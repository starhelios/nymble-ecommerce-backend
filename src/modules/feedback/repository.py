import uuid
from typing import Annotated

from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from src.modules.feedback.models import Feedback
from src.modules.feedback.schema import CreateFeedbackDto
from src.modules.product.models import Product
from src.modules.user.models import User
from src.start.database import db_dependency


class FeedbackRepository:
    def __init__(self, db: db_dependency):
        self.db = db

    def get_feedbacks(self):
        return (
            self.db.query(Feedback).join(Feedback.product).join(Feedback.customer).all()
        )

    def create_feedback(self, create_feedback_dto: CreateFeedbackDto):
        product = (
            self.db.query(Product).filter_by(id=create_feedback_dto.product_id).first()
        )
        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={
                    "message": f"no product found with id: {create_feedback_dto.product_id}"
                },
            )
        customer = (
            self.db.query(User).filter_by(id=create_feedback_dto.customer_id).first()
        )
        if not customer:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={
                    "message": f"no customer found with id: {create_feedback_dto.customer_id}"
                },
            )
        feedback = Feedback(**create_feedback_dto.model_dump(), id=str(uuid.uuid4()))
        self.db.add(feedback)
        self.db.commit()
        self.db.refresh(feedback)
        return feedback


feedback_repository_dependency = Annotated[
    FeedbackRepository, Depends(FeedbackRepository)
]
