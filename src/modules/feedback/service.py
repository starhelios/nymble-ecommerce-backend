from typing import Annotated

from fastapi import Depends

from src.modules.feedback.repository import feedback_repository_dependency
from src.modules.feedback.schema import CreateFeedbackDto


class FeedbackService:
    def __init__(self, feedback_repository: feedback_repository_dependency):
        self.feedback_repository = feedback_repository

    def get_feedbacks(self):
        return self.feedback_repository.get_feedbacks()

    def create_feedback(self, create_feedback_dto: CreateFeedbackDto):
        return self.feedback_repository.create_feedback(create_feedback_dto)


feedback_service_dependency = Annotated[FeedbackService, Depends(FeedbackService)]
