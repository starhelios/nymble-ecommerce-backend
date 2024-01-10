from typing import Annotated

from fastapi import Depends

from src.modules.product.repository import product_repository_dependency
from src.modules.product.schema import CreateProductDto


class ProductService:
    def __init__(self, product_repository: product_repository_dependency) -> None:
        self.product_repository = product_repository

    def get_products(self):
        return self.product_repository.get_products()

    def create_product(self, create_product_dto: CreateProductDto):
        return self.product_repository.create_product(create_product_dto)

    def get_top_selling(self):
        return self.product_repository.get_top_selling()

    def get_product_sales(self, product_id: str):
        return self.product_repository.get_product_sales(product_id)


product_service_dependency = Annotated[ProductService, Depends(ProductService)]
