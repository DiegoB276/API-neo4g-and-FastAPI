from fastapi import APIRouter
from src.schemas.ProviderSchema import Provider
from src.services.ProviderService import(
    Create,
    Obtain,
    Delete,
    Update,
    CompanyByProvider,
    ProductByProvider
)

routeProvider = APIRouter()

@routeProvider.get("/all")
def ObtainAll():
    return Obtain()

@routeProvider.post("/crear")
def createProvider(provider: Provider):
    return Create(provider)

@routeProvider.delete("/eliminar/{nameProvider}")
def DeleteProvider(nameProvider: str):
    return Delete(nameProvider)

@routeProvider.put("/actualizar/{nameProvider}")
def UpdateProvider(nameProvider: str, provider: Provider):
    return Update(nameProvider, provider)

@routeProvider.get("/{name}/companies")
def GetCompaniesByProvider(name: str):
    return CompanyByProvider(name)

@routeProvider.get("/{name}/products")
def GetProductsByProvider(name: str):
    return ProductByProvider(name)