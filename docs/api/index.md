# API Documentation

## Overview

This is the complete API documentation for the Cody backend. All APIs follow RESTful design principles and use JSON format for data exchange.

## Authentication
Please note that the authentication system is not implemented yet. SSO (active directory) will be implemented in the future.
Most APIs require JWT authentication. Please obtain an access token through the login interface first, then include it in the request header:

```
Authorization: Bearer <your-access-token>
```

## Response Format

All API responses follow a unified format:

### Success Response
```json
{
  "code": 200,
  "msg": "success",
  "data": {...}
}
```

### Error Response
```json
{
  "code": 400,
  "msg": "error message",
  "data": null
}
```

### Error Code Description

| Error Code | Description |
|------------|-------------|
| 200 | Success |
| 400 | Request parameter error |
| 401 | Unauthenticated |
| 403 | No permission |
| 404 | Resource not found |
| 422 | Parameter validation failed |
| 429 | Too many requests |
| 500 | Internal server error |



## Health Check

- **Health Status**: `GET /api/v1/base/health`
- **Version Information**: `GET /api/v1/base/version`