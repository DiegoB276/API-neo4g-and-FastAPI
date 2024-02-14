from fastapi import FastAPI, HTTPException
import os
from dotenv import load_dotenv
from src.configs.db import ConnectionDB
from src.schemas.CompanySchema import Company


def Obtain():
    try:
        driver = ConnectionDB()
        session = driver.session()
        query = "MATCH (c:Company) RETURN c"
        results =  session.run(query)
        return results.value()
    except Exception as e:
        return None
    finally:
        driver.close()


def Create(company: Company):
    try:
        driver = ConnectionDB()
        session = driver.session()
        query = "CREATE (c:Company {name: $name, nameCompany: $nameCompany})"
        session.run(query, name=company.name, nameCompany = company.nameCompany)
        return {"message": "Proveedor Creado", "body": company}
    finally:
        driver.close()


def Delete(name: str):
    try:
        driver = ConnectionDB()
        session = driver.session()
        query = "MATCH (c:Company {name: $name}) DETACH DELETE c"
        session.run(query, name = name)
        return {"message": "Compañia Eliminada"}
    finally:
        driver.close()

#No actualiza
def Update(name: str, company:Company):
    try:
        driver = ConnectionDB()
        session = driver.session()
        query = "MATCH (c:Company {name: $name}) SET c.name = $name, c.nameCompany = $nameCompany RETURN c"
        session.run(
            query,
            name=name,
            nameCompany = company.nameCompany
        )
        return {"message": "Compañia actualizada correctamente", "body": company}
    finally:
        driver.close()




