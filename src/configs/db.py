

import os
from dotenv import load_dotenv
from neo4j import GraphDatabase


load_dotenv()
uri = os.getenv("uri")
user = os.getenv("user")
pwd = os.getenv("pwd")

def ConnectionDB():
    try:
        driver = GraphDatabase.driver(uri=uri, auth=(user, pwd))
        return driver
    except Exception as e:
        print(e)
        return None
    finally:
        driver.close()
