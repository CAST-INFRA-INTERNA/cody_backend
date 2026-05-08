## Project Structure

```
Cody/
├── src/                  # Source code directory
│   ├── api/              # API routing layer
│   │   └── v1/           # API version v1
│   ├── services/         # Business logic layer
│   ├── repositories/     # Data access layer
│   ├── models/           # Data models
│   ├── schemas/          # Data validation schemas
│   ├── core/             # Core functionality
│   ├── utils/            # Utility functions
│   ├── main.py           # Application entry point
│   └── workers/          # Background workers
├── tests/                 # Test files
├── migrations/           # Database migration files
├── docs/                 # Documentation source files
├── .env.development      # Development environment variables
├── .env.production       # Production environment variables
├── pyproject.toml        # Project configuration
└── README.md             # Project description
```