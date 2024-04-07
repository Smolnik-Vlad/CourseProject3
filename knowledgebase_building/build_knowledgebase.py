import os

from dotenv import load_dotenv
from neo4j import GraphDatabase

from constant_query import constant_query


def write_data_to_neo4j(uri, user, password, query):
    print(f"uri: {uri} user: {user} password: {password}")
    with GraphDatabase.driver(uri, auth=(user, password)) as driver:
        with driver.session() as session:
            session.run(query)

load_dotenv()


if __name__ == "__main__":
    uri = os.getenv("NEO4J_PATH").replace("neo4j", "localhost")
    user = os.getenv("NEO4J_USER")
    password = os.getenv("NEO4J_PASSWORD")
    query = constant_query
    write_data_to_neo4j(uri, user, password, query)
