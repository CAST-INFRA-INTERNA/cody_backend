## Development Workflow for New Features

When adding new functionality, follow this standard process:

1. **Define Model** (`src/models/admin.py`) - Create Tortoise ORM model
2. **Create Schema** (`src/schemas/`) - Define Pydantic validation schemas
3. **Implement Repository** (`src/repositories/`) - Add data access layer
4. **Write Service** (`src/services/`) - Implement business logic
5. **Add API Routes** (`src/api/v1/`) - Create endpoint handlers
6. **Generate Migration** - Run `uv run aerich migrate --name "feature_name"`
7. **Write Tests** (`tests/`) - Add test coverage