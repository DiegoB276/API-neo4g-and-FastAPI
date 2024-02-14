from fastapi import APIRouter
from src.schemas.ProductSchema import Product
from src.services.ProductService import(
    Obtain,
    Create,
    Delete,
    Update

)

routeProduct = APIRouter()

@routeProduct.get("/all")
def ObtainAll():
    return Obtain()

@routeProduct.post("/crear")
def CreateProduct(product: Product):
    return Create(product)

@routeProduct.delete("/eliminar/{techName}")
def DeleteProduct(techName: str):
    return Delete(techName)

@routeProduct.put("/actualizar/{techName}")
def UpdateProduct(techName: str, product: Product):
    return Update(techName, product)
