## Extension Guide

### Adding New Function Modules

1. **Create Model** (src/models/):
```python
class Product(BaseModel, TimestampMixin):
    name = fields.CharField(max_length=100)
    price = fields.DecimalField(max_digits=10, decimal_places=2)
```

2. **Create Repository** (src/repositories/):
```python
class ProductRepository(BaseRepository):
    def __init__(self):
        super().__init__(Product)
```

3. **Create Service** (src/services/):
```python
class ProductService(BaseService):
    def __init__(self, product_repo: ProductRepository):
        super().__init__(product_repo)
```

4. **Create API** (src/api/v1/):
```python
@router.post("/products")
async def create_product(
    product_data: ProductCreate,
    product_service: ProductService = Depends(get_product_service)
):
    return await product_service.create(product_data)
```

### Custom Middleware

```python
@app.middleware("http")
async def custom_middleware(request: Request, call_next):
    # Before request processing
    response = await call_next(request)
    # After response processing
    return response
```