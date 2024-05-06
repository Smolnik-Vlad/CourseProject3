"""Service to connect to S3."""

import io
import logging

from src.core.settings import settings
from src.repositories.repositories.sessions.s3_session import (
    get_async_boto_client,
)

logger = logging.getLogger(__name__)


class S3Client:
    """Boto3 S3 Client service."""

    SERVICE = "s3"
    BUCKET = settings.s3.BUCKET_NAME

    async def put_object(
        self,
        key: str,
        file_data: bytes,
    ) -> str:
        """
        Put object to S3.

        :param key: file name that represents image on bucket
        :param file_data: image content
        :returns: Image url on bucket
        """
        async with get_async_boto_client(self.SERVICE) as service:
            await service.put_object(
                Bucket=self.BUCKET,
                Key=key,
                Body=io.BytesIO(file_data),
            )
            logger.info(
                f"File uploaded path : "
                f"{settings.s3.ENDPOINT_URL}/{self.BUCKET}/{key}"
            )
            return key

    async def delete_object(self, key: str) -> bool:
        """
        Delete object from S3.

        :param key: file name that represents image on bucket
        :returns: `True` if object was deleted
        """
        async with get_async_boto_client(self.SERVICE) as service:
            await service.delete_object(
                Bucket=self.BUCKET,
                Key=key,
            )
            logger.info(f"ImageMeta {key} was deleted from filestorage.")
            return True

    async def presign_obj(self, key: str) -> str:
        """
        Generate pre-signed urls for object in S3.

        :param key: file name that represents image on bucket
        :returns: pre-signed url for image with key
        """
        #
        async with get_async_boto_client(self.SERVICE) as service:
            url = await service.generate_presigned_url(
                "get_object",
                Params={"Bucket": self.BUCKET, "Key": key},
                ExpiresIn=60 * 60 * 24 * 100,
            )
            return url.replace(
                settings.s3.ENDPOINT_URL, settings.s3.EXTERNAL_URL
            )
