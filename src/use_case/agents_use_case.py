from src.repositories.repository import KnowledgeBaseRepository


class AgentsUseCase:
    def __init__(self, database_repository):
        self.database_repository: KnowledgeBaseRepository = database_repository

    async def get_agents(self):
        res = await self.database_repository.get_agents()
        return res

    async def check_enter(self):
        await self.database_repository.enter_data_in_neo4j()
        return {'enter': 'enter'}

    async def get_data_from_neo4j(self):
        res = await self.database_repository.get_data_from_neo4j()
        return res

    async def create_new_data(self):
        return await self.database_repository.get_data_from_neo4j()

    async def get_picture(
        self,
        name: str | None,
        artist_name: str | None,
        genre: str | None,
        style: str | None,
    ):
        if name:
            return await self.database_repository.get_picture_by_name(name)
        if artist_name:
            return await self.database_repository.get_picture_by_artist_name(
                artist_name
            )
        if genre:
            return await self.database_repository.get_picture_by_genre(genre)
        if style:
            return await self.database_repository.get_picture_by_art_style(
                style
            )
