```bash
# Initialize database (first time setup)
uv run aerich init-db

# Generate migration after model changes
uv run aerich migrate --name "describe_your_changes"

# Apply migrations
uv run aerich upgrade

# View migration history
uv run aerich history

# Initialize database
uv run aerich init-db
```