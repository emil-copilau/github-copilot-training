# GitHub Copilot Project Instructions

## Purpose
This repository is a FastAPI training project for practicing GitHub Copilot workflows. Keep changes simple, explicit, and easy to review.

## Stack
- Python 3.12
- FastAPI + Uvicorn
- Pydantic models
- pytest + pytest-asyncio + httpx
- uv for dependency and command execution

## Repository Conventions
- Main API module is `app/main.py`.
- Tests are under `tests/` and split into:
- `tests/unit/` for unit tests
- `tests/integration/` for endpoint/integration tests
- Shared test fixtures are in `tests/conftest.py`.
- Integration test files must use `@pytest.mark.integration`.

## Coding Rules
1. Prefer `async def` for route handlers and I/O-bound functions.
2. Use explicit type hints for function parameters and return values.
3. Keep API responses as structured JSON-compatible values (dict/list/Pydantic), not ad-hoc text strings for new endpoints.
4. Keep changes focused; avoid unrelated refactors.
5. Follow existing naming and formatting patterns in nearby files.

## Testing Rules
1. Add or update tests for every behavior change.
2. For endpoints, use integration tests with `httpx.AsyncClient`.
3. Cover happy path and negative/validation scenarios.
4. Keep tests deterministic; isolate mutable global state when needed.

## Run Commands
- Install and sync dependencies: `uv sync`
- Run all tests: `uv run pytest`
- Run integration tests only: `uv run pytest tests/integration -q`
- Run unit tests only: `uv run pytest tests/unit -q`
- Run app locally: `uv run uvicorn app.main:app --reload`

## Review Checklist
- Is behavior correct and test-covered?
- Are async and typing conventions followed?
- Are error paths validated?
- Are changes minimal and scoped to the request?