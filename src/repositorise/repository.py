from neo4j import AsyncSession


class KnowledgeBaseRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_agents(self):
        return {'agents': 'agents'}
