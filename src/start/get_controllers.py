from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.modules.admin.controller import admins
from src.modules.feedback.controller import feedbacks
from src.modules.inventory.controller import inventories
from src.modules.order.controller import orders
from src.modules.product.controller import products
from src.modules.user.controller import users


def get_controllers(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(users)
    app.include_router(admins)
    app.include_router(orders)
    app.include_router(products)
    app.include_router(feedbacks)
    app.include_router(inventories)
