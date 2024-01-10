from fastapi import FastAPI

from src.start.get_controllers import get_controllers

app = FastAPI()

get_controllers(app)
