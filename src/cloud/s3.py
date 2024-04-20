"""Service to connect to S3."""

import io
import logging
from contextlib import asynccontextmanager
from typing import AsyncGenerator

import aioboto3
from botocore.exceptions import ClientError

from src.core.exceptions import InfrastructureException
from src.core.settings import settings

logger = logging.getLogger(__name__)


@asynccontextmanager
async def get_async_boto_client(
    service: str,
    endpoint_url: str = settings.s3.ENDPOINT_URL,
    aws_access_key_id: str = settings.s3.MINIO_ACCESS_KEY,
    aws_secret_access_key: str = settings.s3.MINIO_SECRET_KEY,
) -> AsyncGenerator:
    """Boto3 session context manager, catches all errors."""
    async with aioboto3.Session(
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
    ).client(service, endpoint_url=endpoint_url) as client:
        try:
            yield client
        except ClientError as e:
            logger.error(f"Exception occurred during file processing: {e}")
            raise InfrastructureException(detail=f"Failed to upload file: {e}")


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
