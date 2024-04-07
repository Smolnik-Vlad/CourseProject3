from neo4j import AsyncSession


class KnowledgeBaseRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_agents(self):
        return {'agents': 'agents'}

    async def enter_data_in_neo4j(self):
        data = """CREATE (:Person {name: 'Alice', age: 30})"""
        print(self.session)
        await self.session.run(data)

    async def get_data_from_neo4j(self):
        data = await self.session.run("MATCH (n) RETURN n")
        list_of_data = await data.data()
        return list_of_data