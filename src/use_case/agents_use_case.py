from typing import Optional

from src.repositories.repositories.repository import (
    KnowledgeBaseRepository,
)
from src.repositories.repositories.s3 import S3Client
from src.repositories.services.image2text import get_text_from_image
from src.repositories.services.text2image import get_image_from_text
from src.use_case.tags_use_case import TagsUseCase


class AgentsUseCase:
    def __init__(self, database_repository, s3_repository):
        self.database_repository: KnowledgeBaseRepository = database_repository
        self.s3_repository: S3Client = s3_repository
        self.tags_use_case = TagsUseCase()

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

    async def get_artist(self, name: str, picture_name: str):
        if name:
            return await self.database_repository.get_artist_by_name(name)
        if picture_name:
            return await self.database_repository.get_artist_by_picture_name(
                picture_name
            )

    async def get_art_style(
        self, name: Optional[str], picture_name: Optional[str]
    ):
        if name:
            return await self.database_repository.get_art_style_by_name(name)
        if picture_name:
            return (
                await self.database_repository.get_art_style_by_picture_name(
                    picture_name
                )
            )

    async def get_picture_by_id(self, picture_id: int):
        return await self.database_repository.get_picture_by_id(picture_id)

    async def get_artist_by_id(self, artist_id: int):
        return await self.database_repository.get_artist_by_id(artist_id)

    async def get_art_style_by_id(self, art_style_id: int):
        return await self.database_repository.get_art_style_by_id(art_style_id)

    async def generate_picture_by_description(
        self, description: str, picture_name: str
    ):
        image_bytes = await get_image_from_text(description)
        tags = await self.tags_use_case.get_text_tags(description)

        key = await self.s3_repository.put_object(
            picture_name + '.png', image_bytes
        )
        presigned = await self.s3_repository.presign_obj(key)

        await self.database_repository.add_picture_to_db(
            picture_name, description, key, "AI_ART", tags, presigned
        )

        return {'key': key, 'presigned': presigned}

    async def generate_description_by_image(
        self, file_bytes: bytes, picture_name: str
    ):
        description = await get_text_from_image(file_bytes)
        tags = await self.tags_use_case.get_text_tags(description)

        key = await self.s3_repository.put_object(
            picture_name + '.png', file_bytes
        )
        presigned = await self.s3_repository.presign_obj(key)

        await self.database_repository.add_picture_to_db(
            picture_name, description, key, "CUSTOM_ART", tags, presigned
        )
        return description

    async def search_pictures_by_tags(self, description: str):
        description_tags = await self.tags_use_case.get_text_tags(description)
        pictures_data = await self.database_repository.get_pictures_with_tags()
        result_data = [
            (
                record,
                await self.tags_use_case.calculate_similarity(
                    record["picture"]["tags"], description_tags
                ),
            )
            for record in pictures_data
        ]
        result_data.sort(key=lambda x: x[1], reverse=True)
        return [
            record for record, similarity in result_data if similarity >= 0.1
        ]

    async def generate_picture_test(self, prompt: str):
        image = await get_image_from_text(prompt)
        return image

    async def get_tags(self, description: str):
        return await self.tags_use_case.get_text_tags(description)
