
# Cody Backend Template


## Project Features

### Architecture Design

- **Three-Layer Architecture**: API → Service → Repository → Model
- **Dependency Injection**: Based on FastAPI's dependency system
- **Async Support**: Fully asynchronous design supporting high concurrency
- **Type Safety**: Complete Python type annotations

### Security Features

- **JWT Authentication**: Refresh token + Azure AD
- **RBAC Permissions**: Role-Based Access Control

### Core Features

- **User Management**: User CRUD, status management 
- **Role Management**: Role assignment, permission binding
- **Message Broadcasting**: corporate communication orchestration
- **Menu Management**: Dynamic menu configuration (Post MVP)
- **File Management**: Secure file upload/download (Post MVP)
- **Audit Logging**: Complete operation records (Post MVP)
- **Department Management**: Organizational structure management (Totvs)
- **Email Templates**: Customizable email templates
- **AI Chat**: AI-powered chatbot (Post MVP)

### Development Tools

- **UV Package Management**: Fast Python package manager
- **Code Standards**: Black + Ruff + MyPy
- **Test Coverage**: Pytest + Async testing
- **Database Migration**: Aerich migration tool
- **API Documentation**: Automatically generated OpenAPI documentation
- **CI/CD**: GitHub Actions/GitLab CI (post MVP)
- **Containerization**: Docker
- **Monitoring**: Prometheus + Grafana (post MVP)
- **Logging**: Stack (post MVP)
- **Task Scheduling**: TaskIQ + Redis

## Technology Stack

=== "Backend Framework"

    - **FastAPI**: Modern, high-performance web framework
    - **Tortoise ORM**: Asynchronous ORM framework
    - **Pydantic**: Data validation and settings management
    - **JWT**: JSON Web Token authentication
    - **Jinja2 + MJML**: MJML for Email template rendering and Jinja2 for template management
    - **TaskIQ + Redis**: Asynchronous task queue for background processing 
    - **Azure AD**: Azure Active Directory for authentication SSO integration

=== "Database"

    - **PostgreSQL**: Recommended for production
    - **SQLite**: Default for development
    - **Redis**: Caching and session storage
    - **Aerich**: Database migration tool

=== "Development Tools"

    - **UV**: Python package manager
    - **Black**: Code formatting
    - **Ruff**: Code linting
    - **MyPy**: Type checking
    - **Pytest**: Testing framework

=== "Deployment & Operations"

    - **Docker**: Containerized deployment 
    - **GitHub Actions**: CI/CD automation
    - **Uvicorn**: ASGI server
    

