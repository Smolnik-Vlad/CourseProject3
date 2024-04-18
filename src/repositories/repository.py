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

    async def get_picture_by_artist_name(self, artist_name: str):
        stmt = (
            "MATCH (n:Artist{name:'%s'})-"
            "[r:`Создал`]-(picture:Picture) RETURN picture" % artist_name
        )
        data = await self.session.run(stmt)
        return await data.data()

    async def get_picture_by_genre(self, genre: str):
        stmt = "MATCH (picture:Picture{genre:'%s'}) RETURN picture" % genre
        data = await self.session.run(stmt)
        return await data.data()

    async def get_picture_by_name(self, name: str):
        stmt = "MATCH (picture:Picture{name:'%s'}) RETURN picture" % name
        data = await self.session.run(stmt)
        return await data.data()

    async def get_picture_by_art_style(self, style: str):
        stmt = (
            "MATCH (picture:Picture)-"
            "[r:`Написана_в_стиле`]-(s:ArtStyle{name: '%s'}) RETURN picture"
            % style
        )
        data = await self.session.run(stmt)
        return await data.data()
