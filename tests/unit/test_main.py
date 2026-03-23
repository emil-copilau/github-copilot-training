import pytest

from app.main import TaskStatus, fetch_all_tasks, generate_productivity_report


@pytest.mark.asyncio
async def test_fetch_all_tasks_returns_non_empty_list() -> None:
    tasks = await fetch_all_tasks()

    assert isinstance(tasks, list)
    assert len(tasks) > 0


@pytest.mark.asyncio
async def test_fetch_all_tasks_returns_task_models_with_expected_fields() -> None:
    tasks = await fetch_all_tasks()
    first_task = tasks[0]

    assert isinstance(first_task.task_id, int)
    assert isinstance(first_task.title, str)
    assert isinstance(first_task.status, TaskStatus)
    assert isinstance(first_task.hours_spent, float)


@pytest.mark.asyncio
async def test_generate_productivity_report_returns_expected_totals() -> None:
    report = await generate_productivity_report()

    assert report.total_tasks == 3
    assert report.completed_tasks == 1
    assert report.total_hours_spent == 23.5
    assert report.completion_rate == 0.33


@pytest.mark.asyncio
async def test_generate_productivity_report_completion_rate_is_consistent_with_completed_tasks() -> None:
    report = await generate_productivity_report()

    expected_completion_rate = round(report.completed_tasks / report.total_tasks, 2)
    assert report.completion_rate == expected_completion_rate
