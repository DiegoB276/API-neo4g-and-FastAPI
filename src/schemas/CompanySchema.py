from pydantic import BaseModel, Field


class Company(BaseModel):
    name: str = Field()
    nameCompany: str = Field()
