---
applyTo: "**/*.py"
---

# Project Development Instructions

## Scope
Use these instructions for general development tasks in this repository.

## Project Context
- FastAPI training project for GitHub Copilot workflows.
- Python 3.12 runtime.
- Dependency management and command execution with uv.

## Code Location
- API application: app/main.py
- Unit tests: tests/unit/
- Integration tests: tests/integration/
- Shared fixtures: tests/conftest.py

## Implementation Standards
1. Prefer async route handlers and async I/O functions.
2. Use explicit type hints on function signatures.
3. Keep changes focused and minimal.
4. Preserve existing naming and style in the touched files.

## API and Validation Standards
1. Return structured JSON-compatible values (dict, list, or Pydantic models).
2. Include clear validation and error handling paths for new behaviors.

## Testing Standards
1. Add tests for each change in behavior.
2. Use httpx.AsyncClient for endpoint integration tests.
3. Mark integration tests with @pytest.mark.integration.
4. Cover both happy path and negative scenarios.
5. Keep tests deterministic and independent.

## Common Commands
- uv sync
- uv run pytest
- uv run pytest tests/integration -q
- uv run pytest tests/unit -q
- uv run uvicorn app.main:app --reload
