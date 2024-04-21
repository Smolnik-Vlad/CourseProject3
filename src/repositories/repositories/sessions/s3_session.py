import logging
from contextlib import asynccontextmanager
from typing import AsyncGenerator

import aioboto3
from aiohttp import ClientError

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
