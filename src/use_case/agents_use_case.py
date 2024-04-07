from src.repositories.repository import KnowledgeBaseRepository
from src.repositories.sessions import async_session_maker


class AgentsUseCase:

    @staticmethod
    async def get_agents():
        async with async_session_maker() as session:
            res = await KnowledgeBaseRepository(session).get_agents()
        return res

    # async def check_enter(self):
    #     await self.database_repository.enter_data_in_neo4j()
    #     return {'enter': 'enter'}
    #
    @staticmethod
    async def get_data_from_neo4j():
        async with async_session_maker() as session:
            res = await KnowledgeBaseRepository(session).get_data_from_neo4j()
        return res
    #
    # async def create_new_data(self):
    #     return await self.database_repository.get_data_from_neo4j()
