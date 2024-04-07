from contextlib import asynccontextmanager

from neo4j import AsyncGraphDatabase, AsyncSession, AsyncDriver

from src.core.settings import settings


@asynccontextmanager
async def async_session_maker():
    async with AsyncGraphDatabase.driver(
            uri=settings.NEO4J_PATH,
            auth=(settings.NEO4J_USER, settings.NEO4J_PASSWORD)
    ) as session_maker:
        print(f"uri: {settings.NEO4J_PATH} user: {settings.NEO4J_USER} password: {settings.NEO4J_PASSWORD}")
        yield session_maker.session()

