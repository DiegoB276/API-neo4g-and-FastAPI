from fastapi import FastAPI, HTTPException
import os
from dotenv import load_dotenv
from src.configs.db import ConnectionDB
from src.schemas.ProviderSchema import Provider


def Obtain():
    try:
        driver = ConnectionDB()
        session = driver.session()
        query = "MATCH (p:Provider) RETURN p"
        results =  session.run(query)
        return results.value()
    except Exception as e:
        return None
    finally:
        driver.close()


def Create(provider: Provider):
    try:
        driver = ConnectionDB()
        session = driver.session()
        query = "CREATE (p:Provider {name: $name, nameProvider: $nameProvider, email: $email})"
        session.run(query, name=provider.name, nameProvider = provider.nameProvider, email = provider.email)
        return {"message": "Proveedor Creado", "body": provider}
    finally:
        driver.close()


def Delete(nameProvider: str):
    try:
        driver = ConnectionDB()
        session = driver.session()
        query = "MATCH (p:Provider {nameProvider: $nameProvider}) DETACH DELETE p"
        session.run(query, nameProvider = nameProvider)
        return {"message": "Proveedor Eliminado"}
    finally:
        driver.close()

#No actualiza
def Update(nameProvider: str, provider:Provider):
    try:
        driver = ConnectionDB()
        session = driver.session()
        query = "MATCH (p:Provider {nameProvider: $nameProvider}) SET p.name = $name, p.nameProvider = $nameProvider, p.email = $email RETURN p"
        session.run(
            query,
            name=provider.name,
            nameProvider = nameProvider,
            email=provider.email
        )
        return {"message": "Proveedor actualizado correctamente", "body": provider}
    finally:
        driver.close()



def CompanyByProvider(name: str):
    try:
        driver = ConnectionDB()
        session = driver.session()
        query = "MATCH (p:Provider {name: $name})--(c:Company) RETURN c"
        results = session.run(query, name=name)
        data = results.value()
        return data
    finally:
        driver.close()
        

def ProductByProvider(name: str):
    try:
        driver = ConnectionDB()
        session = driver.session()
        query = "MATCH (p:Provider {name: $name})--(n:Product) RETURN n"
        results = session.run(query, name=name)
        data = results.value()
        return data
    finally:
        driver.close()