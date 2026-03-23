from typing import AsyncGenerator, Generator

import pytest
import pytest_asyncio
from httpx import ASGITransport, AsyncClient

from app.main import app as fastapi_app


@pytest.fixture
def app():
    return fastapi_app


@pytest_asyncio.fixture
async def client(app) -> AsyncGenerator[AsyncClient, None]:
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://testserver") as async_client:
        yield async_client


@pytest.fixture
def db_session() -> Generator[None, None, None]:
    # Placeholder fixture for future database-backed tests.
    yield None


@pytest.fixture
def auth_token() -> str:
    # Placeholder fixture for endpoints that require authentication.
    return "test-auth-token"
