#### Pre-commit Hooks (Automated)
```bash
# Hooks are automatically installed and configured during uv sync
# They run automatically on every git commit to ensure code quality

# Manually run all checks
uv run pre-commit run --all-files

# Disable hooks (if not needed)
uv run pre-commit uninstall

# Skip single check (for emergency commits)
git commit --no-verify -m "urgent fix"
```

#### Manual Check Commands
```bash
# Code checking and auto-fix (replaces black + isort)
uv run ruff check --fix src/

# Code formatting
uv run ruff format src/

# Type checking (optional)
uv run mypy src/
```

 **Detailed Configuration**: refer to [pre-commit-guide.md](../../docs/pre-commit-guide.md)