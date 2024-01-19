import pytest
from httpx import AsyncClient

from main import app
import pytest_asyncio


@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"


@pytest_asyncio.fixture(scope="session", autouse=False)
async def test_client():
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client
    await client.aclose()


@pytest.fixture
def test_record_data():
    return {
        "user_id": "user123",
        "tool_id": "tool456",
    }


@pytest.mark.asyncio
async def test_all(test_client, test_record_data):
    response = await test_client.post("/records/", json=test_record_data)
    assert response.status_code == 200
    assert "record_id" in response.json()

    response = await test_client.get("/records/")
    assert response.status_code == 200
    assert "records" in response.json()

    response = await test_client.get("/records/?skip=0&limit=1")
    assert response.status_code == 200
    assert "records" in response.json()
    assert len(response.json()["records"]) == 1
