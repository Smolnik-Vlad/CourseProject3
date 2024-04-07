from src.repositorise.repository import KnowledgeBaseRepository


class AgentsUseCase:
    def __init__(self, database_repository):
        self.database_repository: KnowledgeBaseRepository = database_repository

    async def get_agents(self):
        res = await self.database_repository.get_agents()
        return res
