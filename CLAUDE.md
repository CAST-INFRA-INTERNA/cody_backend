
# CLAUDE.md


## Project Overview

CODY is a corporate communication orchestration platform designed for high performance, rigorous governance, and data flexibility. It provides a unified interface for managing various communication channels, including email, messaging apps, and social media. CODY enables businesses to streamline their communication processes, enforce compliance policies, and gain insights through analytics.


## Common Commands

### Database Operations
refer to [Database Management](docs/guide/database.md)

### Testing
refer to [Testing Guide](docs/guide/tests.md)

### Code Quality

refer to [Code Quality Guide](docs/guide/code_quality.md)

### Documentation
for documentation writing and maintenance,
refer to [Documentation Guide](docs/guide/documentation.md)

## Architecture

### Architecture Overview
This is an enterprise-grade FastAPI backend template with a clean three-layer architecture (API → Service → Repository → Model). It includes built-in RBAC permission management, user management, file management, and other core enterprise features. The project uses UV for package management and focuses on providing a clean, extensible backend framework.
for more details,
refer to [Architecture Overview](docs/architecture/architecure_overview.md)

### Project Structure
refer to [Project Structure](docs/architecture/project_structure.md)

### Development Workflow
For a simple and efficient development workflow,
refer to [Development Workflow](docs/guide/development_workflow.md)


### Development Server
```bash
# Run development server with hot reload
uv run uvicorn src:app --reload --host 0.0.0.0 --port 8000
```

## Database Best Practices
- Models inherit from `BaseModel` and `TimestampMixin` for consistency
- Use `select_related()` for foreign key preloading
- Use `prefetch_related()` for many-to-many optimization
- Add indexes on frequently queried fields
- String references for relationships to avoid circular imports: `fields.ForeignKeyField("models.User")`


## Important Notes!
- All routes are async - use `await` for database operations
- Repository pattern is used for data access - avoid direct model queries in services
- Services handle business logic and permissions - keep routes thin
- Use dependency injection for authentication: `current_user: User = DependAuth`
- For admin-only endpoints use: `current_user: User = SuperUserRequired`
- When modifying models, always generate and apply migrations
- The project uses UV for dependency management - avoid pip directly

