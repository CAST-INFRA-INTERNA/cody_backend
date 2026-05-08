## Design Patterns

### 1. Dependency Injection
Using FastAPI's dependency injection system:

```python
# Dependency definition
def get_user_service() -> UserService:
    return UserService(user_repository)

# Using dependency
@router.post("/users")
async def create_user(
    user_data: UserCreate,
    user_service: UserService = Depends(get_user_service)
):
    return await user_service.create_user(user_data)
```

### 2. Repository Pattern
Encapsulating data access logic:

```python
class BaseRepository:
    def __init__(self, model: Type[Model]):
        self.model = model

    async def create(self, data: dict) -> Model:
        return await self.model.create(**data)

    async def get_by_id(self, id: int) -> Optional[Model]:
        return await self.model.get_or_none(id=id)
```

### 3. Service Layer Pattern
Encapsulating business logic:

```python
class BaseService:
    def __init__(self, repository: BaseRepository):
        self.repository = repository

    async def create(self, data: BaseModel) -> Model:
        # Business logic processing
        validated_data = self.validate_data(data)
        return await self.repository.create(validated_data)
```