import copy

import pytest
from httpx import AsyncClient

from app.main import MOCK_TASKS


@pytest.fixture(autouse=True)
def reset_mock_tasks() -> None:
    original_tasks = copy.deepcopy(MOCK_TASKS)
    yield
    MOCK_TASKS.clear()
    MOCK_TASKS.update(original_tasks)


@pytest.mark.asyncio
@pytest.mark.integration
async def test_status_returns_200(client: AsyncClient) -> None:
    response = await client.get("/status")

    assert response.status_code == 200


@pytest.mark.asyncio
@pytest.mark.integration
async def test_status_returns_expected_json_body(client: AsyncClient) -> None:
    response = await client.get("/status")

    assert response.json() == {"status": "ok"}


@pytest.mark.asyncio
@pytest.mark.integration
async def test_status_response_content_type_is_json(client: AsyncClient) -> None:
    response = await client.get("/status")

    assert "application/json" in response.headers["content-type"]


@pytest.mark.asyncio
@pytest.mark.integration
async def test_status_rejects_post_method(client: AsyncClient) -> None:
    response = await client.post("/status")

    assert response.status_code == 405


@pytest.mark.asyncio
@pytest.mark.integration
async def test_status_rejects_put_method(client: AsyncClient) -> None:
    response = await client.put("/status")

    assert response.status_code == 405


@pytest.mark.asyncio
@pytest.mark.integration
async def test_status_rejects_delete_method(client: AsyncClient) -> None:
    response = await client.delete("/status")

    assert response.status_code == 405


@pytest.mark.asyncio
@pytest.mark.integration
async def test_status_is_idempotent_across_multiple_calls(client: AsyncClient) -> None:
    responses = [await client.get("/status") for _ in range(3)]

    assert all(response.status_code == 200 for response in responses)
    assert all(response.json() == {"status": "ok"} for response in responses)


@pytest.mark.asyncio
@pytest.mark.integration
async def test_status_has_no_required_auth_headers(client: AsyncClient) -> None:
    response = await client.get("/status", headers={})

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


@pytest.mark.asyncio
@pytest.mark.integration
async def test_task_status_returns_task_status_for_existing_task(client: AsyncClient) -> None:
    response = await client.get("/task/1/status")

    assert response.status_code == 200
    assert response.json() == {"task_id": 1, "status": "complete"}


@pytest.mark.asyncio
@pytest.mark.integration
async def test_task_status_returns_404_for_missing_task(client: AsyncClient) -> None:
    response = await client.get("/task/999/status")

    assert response.status_code == 404
    assert response.json() == {"detail": "Task 999 not found"}


@pytest.mark.asyncio
@pytest.mark.integration
async def test_task_status_rejects_non_integer_task_id(client: AsyncClient) -> None:
    response = await client.get("/task/abc/status")

    assert response.status_code == 422


@pytest.mark.asyncio
@pytest.mark.integration
async def test_report_returns_expected_productivity_metrics(client: AsyncClient) -> None:
    response = await client.get("/report")

    assert response.status_code == 200
    assert response.json() == {
        "total_tasks": 3,
        "completed_tasks": 1,
        "total_hours_spent": 23.5,
        "completion_rate": 0.33,
    }


@pytest.mark.asyncio
@pytest.mark.integration
async def test_log_task_returns_200_on_valid_payload(client: AsyncClient) -> None:
    payload = {"task_id": 123, "title": "Draft API docs", "status": "pending", "hours_spent": 2.5}

    response = await client.post("/log_task", json=payload)

    assert response.status_code == 200


@pytest.mark.asyncio
@pytest.mark.integration
async def test_log_task_assigns_new_task_id_ignoring_input_id(client: AsyncClient) -> None:
    before_tasks = (await client.get("/tasks")).json()
    expected_id = max(task["task_id"] for task in before_tasks) + 1

    payload = {"task_id": 9999, "title": "Review pull request", "status": "in_progress", "hours_spent": 1.0}
    response = await client.post("/log_task", json=payload)

    assert response.status_code == 200
    assert response.text == f"Task ID {expected_id} logged successfully."


@pytest.mark.asyncio
@pytest.mark.integration
async def test_log_task_increases_tasks_count_by_one(client: AsyncClient) -> None:
    before_count = len((await client.get("/tasks")).json())

    payload = {"task_id": 55, "title": "Implement pagination", "status": "pending", "hours_spent": 3.0}
    response = await client.post("/log_task", json=payload)
    after_count = len((await client.get("/tasks")).json())

    assert response.status_code == 200
    assert after_count == before_count + 1


@pytest.mark.asyncio
@pytest.mark.integration
async def test_log_task_persists_created_task_in_tasks_endpoint(client: AsyncClient) -> None:
    payload = {"task_id": 11, "title": "Persisted task", "status": "complete", "hours_spent": 4.25}

    response = await client.post("/log_task", json=payload)
    tasks = (await client.get("/tasks")).json()

    assert response.status_code == 200
    assert any(
        task["title"] == payload["title"]
        and task["status"] == payload["status"]
        and task["hours_spent"] == payload["hours_spent"]
        for task in tasks
    )


@pytest.mark.asyncio
@pytest.mark.integration
async def test_log_task_defaults_status_when_missing(client: AsyncClient) -> None:
    payload = {"task_id": 77, "title": "Default status check", "hours_spent": 1.5}

    response = await client.post("/log_task", json=payload)
    tasks = (await client.get("/tasks")).json()
    created_task = next(task for task in tasks if task["title"] == payload["title"])

    assert response.status_code == 200
    assert created_task["status"] == "pending"


@pytest.mark.asyncio
@pytest.mark.integration
async def test_log_task_defaults_hours_spent_when_missing(client: AsyncClient) -> None:
    payload = {"task_id": 78, "title": "Default hours check", "status": "pending"}

    response = await client.post("/log_task", json=payload)
    tasks = (await client.get("/tasks")).json()
    created_task = next(task for task in tasks if task["title"] == payload["title"])

    assert response.status_code == 200
    assert created_task["hours_spent"] == 0.0


@pytest.mark.asyncio
@pytest.mark.integration
async def test_log_task_rejects_invalid_status_value(client: AsyncClient) -> None:
    payload = {"task_id": 1, "title": "Invalid status", "status": "done", "hours_spent": 1.0}

    response = await client.post("/log_task", json=payload)

    assert response.status_code == 422


@pytest.mark.asyncio
@pytest.mark.integration
async def test_log_task_rejects_missing_required_title(client: AsyncClient) -> None:
    payload = {"task_id": 1, "status": "pending", "hours_spent": 1.0}

    response = await client.post("/log_task", json=payload)

    assert response.status_code == 422


@pytest.mark.asyncio
@pytest.mark.integration
async def test_log_task_rejects_missing_required_task_id_field(client: AsyncClient) -> None:
    payload = {"title": "Missing id", "status": "pending", "hours_spent": 1.0}

    response = await client.post("/log_task", json=payload)

    assert response.status_code == 422


@pytest.mark.asyncio
@pytest.mark.integration
async def test_log_task_rejects_invalid_hours_spent_type(client: AsyncClient) -> None:
    payload = {"task_id": 1, "title": "Invalid hours", "status": "pending", "hours_spent": "many"}

    response = await client.post("/log_task", json=payload)

    assert response.status_code == 422


@pytest.mark.asyncio
@pytest.mark.integration
async def test_log_task_rejects_invalid_task_id_type(client: AsyncClient) -> None:
    payload = {"task_id": "abc", "title": "Invalid id", "status": "pending", "hours_spent": 1.0}

    response = await client.post("/log_task", json=payload)

    assert response.status_code == 422


@pytest.mark.asyncio
@pytest.mark.integration
async def test_log_task_response_message_contains_created_id(client: AsyncClient) -> None:
    before_tasks = (await client.get("/tasks")).json()
    expected_id = max(task["task_id"] for task in before_tasks) + 1

    payload = {"task_id": 500, "title": "Message contains id", "status": "pending", "hours_spent": 0.25}
    response = await client.post("/log_task", json=payload)

    assert response.status_code == 200
    assert str(expected_id) in response.text
    assert "logged successfully" in response.text
