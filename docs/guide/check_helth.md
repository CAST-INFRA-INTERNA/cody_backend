## Check Health Status

```bash
curl http://localhost:8000/api/v1/base/health
```

Expected Response:

```json
{
  "status": "healthy",
  "timestamp": "01-01-2024T00:00:00Z",
  "version": "1.0.0",
  "environment": "development",
  "service": "Cody Backend"
}
```