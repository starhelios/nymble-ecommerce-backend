from fastapi import APIRouter

from src.modules.feedback.schema import CreateFeedbackDto
from src.modules.feedback.schema import FeedbackResponse
from src.modules.feedback.schema import FeedbackWithProductResponse
from src.modules.feedback.service import feedback_service_dependency

feedbacks = APIRouter(prefix="/api/feedbacks", tags=["feedbacks"])


@feedbacks.get("/", response_model=list[FeedbackWithProductResponse])
def get_feedbacks(feedback_service: feedback_service_dependency):
    return feedback_service.get_feedbacks()


@feedbacks.post("/", response_model=FeedbackResponse)
def create_feedback(
    feedback_service: feedback_service_dependency,
    create_feedback_dto: CreateFeedbackDto,
):
    return feedback_service.create_feedback(create_feedback_dto)
