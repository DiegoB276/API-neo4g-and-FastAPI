from fastapi import FastAPI, HTTPException
import os
from dotenv import load_dotenv
from src.configs.db import ConnectionDB
from src.schemas.ProductSchema import Product


def Obtain():
    try:
        driver = ConnectionDB()
        session = driver.session()
        query = "MATCH (p:Product) RETURN p"
        results =  session.run(query)
        return results.value()
    except Exception as e:
        return None
    finally:
        driver.close()


def Create(product: Product):
    try:
        driver = ConnectionDB()
        session = driver.session()
        query = "CREATE (p:Product {name: $name, techName: $techName, typeProduct: $typeProduct})"
        session.run(query, name=product.name, techName = product.techName, typeProduct = product.typeProduct)
        return {"message": "Producto Creado", "body": product}
    finally:
        driver.close()


def Delete(techName: str):
    try:
        driver = ConnectionDB()
        session = driver.session()
        query = "MATCH (p:Product {techName: $techName}) DETACH DELETE p"
        session.run(query, techName = techName)
        return {"message": "Producto Eliminado"}
    finally:
        driver.close()



#No actualiza
def Update(techName: str, product:Product):
    try:
        driver = ConnectionDB()
        session = driver.session()
        query = "MATCH (p:Product {techName: $techName}) SET p.name = $name, p.techName = $techName, p.typeProduct = $typeProduct RETURN p"
        session.run(
            query,
            name=product.name,
            techName = techName,
            typeProduct=product.typeProduct
        )
        return {"message": "Producto actualizado correctamente", "body": product}
    finally:
        driver.close()
