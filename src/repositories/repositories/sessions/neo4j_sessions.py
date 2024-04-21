from neo4j import AsyncDriver, AsyncGraphDatabase, AsyncSession

from src.core.settings import settings


async def session_knowledge_base():
    async with AsyncGraphDatabase.driver(
        uri=settings.NEO4J_PATH,
        auth=(settings.NEO4J_USER, settings.NEO4J_PASSWORD),
    ) as driver:
        print(
            f"uri: {settings.NEO4J_PATH} user: "
            f"{settings.NEO4J_USER} password: {settings.NEO4J_PASSWORD}"
        )
        async with driver.session() as session:
            yield session
