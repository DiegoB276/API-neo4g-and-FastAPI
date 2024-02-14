# Modelos de datos
from pydantic import BaseModel, Field


class Provider(BaseModel):
    name: str = Field()
    nameProvider: str = Field()
    email: str = Field()
