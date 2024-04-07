from neo4j import AsyncGraphDatabase, AsyncSession

from src.core.settings import settings


async def get_session_knowledge_base() -> AsyncSession:
    async with AsyncGraphDatabase(settings.database_url,
                                  auth=(settings.database_user, settings.database_password)) as driver:
        async with driver.session(database=settings.database_name) as session:
            yield session
