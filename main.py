from fastapi import FastAPI
from src.routes.ProviderRoute import routeProvider
from src.routes.ProductRoute import routeProduct
from src.routes.CompanyRoute import routeCompany


app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hola Mundo"}


app.include_router(routeProvider, prefix="/api/v1/providers", tags=["Providers"])
app.include_router(routeProduct, prefix="/api/v1/products", tags=["Products"])
app.include_router(routeCompany, prefix="/api/v1/companies", tags=["Companies"])
