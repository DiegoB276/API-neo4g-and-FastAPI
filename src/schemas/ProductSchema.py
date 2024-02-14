from pydantic import BaseModel, Field


class Product(BaseModel):
    name: str = Field()
    techName: str = Field()
    typeProduct: str = Field()
