import os

from constant_query import constant_query
from dotenv import load_dotenv
from neo4j import GraphDatabase


def write_data_to_neo4j(uri, user, password, query: list):
    print(f"uri: {uri} user: {user} password: {password}")
    with GraphDatabase.driver(uri, auth=(user, password)) as driver:
        with driver.session() as session:
            for q in query:
                if q:
                    session.run(q)


load_dotenv()

if __name__ == "__main__":
    uri = os.getenv("NEO4J_PATH")
    user = os.getenv("NEO4J_USER")
    password = os.getenv("NEO4J_PASSWORD")
    constant_query = constant_query.replace("\n", "")
    list_of_queries = constant_query.split(";")
    write_data_to_neo4j(uri, user, password, list_of_queries)
