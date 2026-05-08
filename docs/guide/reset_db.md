## Delete the database file and migration records:

```bash
# SQLite
rm cody_db.db

# Reinitialize
uv run aerich init-db
```