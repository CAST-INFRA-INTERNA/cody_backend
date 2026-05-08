# Edit the `.env.development` file to configure necessary environment variables:

```env
# Application Configuration
APP_ENV=development
SECRET_KEY=your-secret-key-here
DEBUG=True

# Database Configuration
DB_ENGINE=sqlite
DB_NAME=fastapi_template.db

# JWT Configuration
JWT_ACCESS_TOKEN_EXPIRE_MINUTES=240
JWT_REFRESH_TOKEN_EXPIRE_DAYS=7

# CORS Configuration
CORS_ORIGINS=http://localhost:3000,http://localhost:8080
```