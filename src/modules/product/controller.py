from fastapi import APIRouter

from src.modules.product.schema import CreateProductDto
from src.modules.product.schema import ProductResponse
from src.modules.product.schema import ProductSalesResponse
from src.modules.product.schema import TopSellingProductResponse
from src.modules.product.service import product_service_dependency


products = APIRouter(prefix="/api/products", tags=["products"])


@products.get("/", response_model=list[ProductResponse])
def get_products(product_service: product_service_dependency):
    return product_service.get_products()


@products.post("/", response_model=ProductResponse)
def create_product(
    product_service: product_service_dependency, create_product_dto: CreateProductDto
):
    return product_service.create_product(create_product_dto)


@products.get("/top-selling", response_model=list[TopSellingProductResponse])
def get_top_selling(product_service: product_service_dependency):
    return product_service.get_top_selling()


@products.get("/product-sales", response_model=ProductSalesResponse)
def get_product_sales(product_id: str, product_service: product_service_dependency):
    return product_service.get_product_sales(product_id)
