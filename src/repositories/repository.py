from urllib.parse import quote

from neo4j import AsyncSession


class KnowledgeBaseRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_agents(self):
        return {'agents': 'agents'}

    async def get_pictures_with_tags(self):
        stmt = (
            "MATCH (picture:Picture) WHERE (picture.tags) "
            "IS NOT NULL RETURN picture"
        )
        data = await self.session.run(stmt)
        return await data.data()

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

    async def get_artist_by_name(self, name: str):
        stmt = "MATCH (artist:Artist{name:'%s'}) RETURN artist" % name
        data = await self.session.run(stmt)
        return await data.data()

    async def get_artist_by_picture_name(self, picture_name: str):
        stmt = (
            "MATCH (artist:Artist)-[r:`Создал`]-(picture:Picture{name:'%s'})\
            RETURN artist"
            % picture_name
        )
        data = await self.session.run(stmt)
        return await data.data()

    async def get_art_style_by_name(self, name: str):
        stmt = "MATCH (style:ArtStyle{name:'%s'}) RETURN style" % name
        data = await self.session.run(stmt)
        return await data.data()

    async def get_art_style_by_picture_name(self, picture_name: str):
        stmt = (
            "MATCH (p:Picture{name: '%s'})-[r:`Написана_в_стиле`]-\
            (style:ArtStyle) RETURN style"
            % picture_name
        )
        data = await self.session.run(stmt)
        return await data.data()

    async def get_picture_by_id(self, picture_id: int):
        stmt = (
            "MATCH (picture:Picture) WHERE id(picture) = %s RETURN picture"
            % picture_id
        )
        data = await self.session.run(stmt)
        return await data.data()

    async def get_artist_by_id(self, artist_id: int):
        stmt = (
            "MATCH (artist:Artist) WHERE id(artist) = %s RETURN artist"
            % artist_id
        )
        data = await self.session.run(stmt)
        return await data.data()

    async def get_art_style_by_id(self, art_style_id: int):
        stmt = (
            "MATCH (style:ArtStyle) WHERE id(style) = %s RETURN style"
            % art_style_id
        )
        data = await self.session.run(stmt)
        return await data.data()

    async def add_picture_to_db(
        self, picture_name, information, image, genre, tags, image_link
    ):
        data = (
            "CREATE (picture:Picture {name: '%s', information: '%s', image: '%s',\
             genre: '%s', tags: %s, image_link: '%s'})"
            % (
                picture_name,
                information,
                image,
                genre,
                str(tags),
                quote(image_link),
            )
        )
        await self.session.run(data)
