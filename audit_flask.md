# Python Project Audit Report

- **Generated:** 2025-09-22T16:40:40+00:00
- **Repo Path:** `/var/folders/xs/z59w57g118v32dht04blnmbc0000gn/T/repo_i7bete0w`

## Packaging
- `pyproject.toml`: Yes ✅
- `setup.py`: No ❌
- `setup.cfg`: No ❌

## Dependencies
- Found dependency files:
  - `pyproject.toml`
  - `uv.lock`

## Tests
- Test directories:
  - `tests`
- Pytest config present: Yes ✅

## Test Run Results
- Test run skipped.

## Ruff Linting
```
warning: The following rules have been removed and ignoring them has no effect:
    - UP038

warning: Invalid rule code provided to `# noqa` at src/flask/sessions.py:110: B950
warning: Invalid rule code provided to `# noqa` at src/flask/app.py:273: B950
warning: Invalid rule code provided to `# noqa` at src/flask/app.py:1480: B001
All checks passed!
```

## Pyupgrade
```
pyupgrade available but not applied (use --apply-fixes).
```
