
## Log in using the default administrator account:

```bash
curl -X POST "http://localhost:8000/api/v1/base/access_token" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "admin",
    "password": "[PASSWORD]"
  }'
```

## Testing
```bash
# Run all tests
uv run pytest

# Run specific test file
uv run pytest tests/test_users.py

# Run with coverage report
uv run pytest --cov=src --cov-report=html
```