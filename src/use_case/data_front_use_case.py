from src.repositories.repositories.repository import (
    KnowledgeBaseRepository,
)


class DataFrontUseCase:
    def __init__(self, database_repository):
        self.database_repository: KnowledgeBaseRepository = database_repository

    async def get_front_features(self, dark_theme: bool):
        theme = 'dark_theme' if dark_theme else 'light_theme'
        data = await self.database_repository.get_theme_features(theme)
        processed_data = data[0]['theme']
        return processed_data
