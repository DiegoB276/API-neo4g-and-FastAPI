from fastapi import APIRouter
from src.schemas.CompanySchema import Company
from src.services.CompanyService import(
    Obtain,
    Create,
    Delete,
    Update

)

routeCompany = APIRouter()

@routeCompany.get("/all")
def ObtainAll():
    return Obtain()


@routeCompany.post("/crear")
def createCompany(company: Company):
    return Create(company)

@routeCompany.delete("/eliminar/{name}")
def DeleteProvider(name: str):
    return Delete(name)


@routeCompany.put("/actualizar/{name}")
def UpdateCompany(name: str, company: Company):
    return Update(name, company)
