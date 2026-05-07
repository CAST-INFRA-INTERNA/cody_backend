The project follows a clean three-layer architecture with clear separation of concerns:

```
┌─────────────────────────────────────────────────────────────┐
│                        API Layer                            │
│  (src/api/v1/) - Routes, parameter validation, responses    │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                      Service Layer                          │
│  (src/services/) - Business logic, permissions, validation  │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                   Repository Layer                          │
│  (src/repositories/) - Data access, CRUD operations         │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                      Model Layer                            │
│  (src/models/) - Tortoise ORM models, database schemas      │
└─────────────────────────────────────────────────────────────┘
```

### Key Design Principles
- **Single Responsibility**: Each layer handles only its own logic
- **Dependency Injection**: Managed through FastAPI's dependency system
- **Type Safety**: Comprehensive Python type annotations throughout
- **Async First**: All I/O operations are asynchronous
- **Security First**: Multiple built-in security mechanisms

### Core Components

- **Authentication**: SSO (Azure AD) + JWT-based with access tokens
- **Authorization**: RBAC system with roles, menus, and API permissions
- **Audit Logging**: Comprehensive user activity tracking
- **Caching**: Redis integration with smart caching strategies
- **Task Scheduling**: TaskIQ + Redis for background processing and message broadcasting (email templates, etc.)
