# Pre-commit Hooks Usage Guide

This project uses pre-commit hooks to ensure code quality and consistency.

## What are Pre-commit Hooks?

Pre-commit hooks are scripts that automatically run before each `git commit` to:
- Automatically format code
- Check code quality
- Prevent low-quality code from being committed

## Enabled Checks

### Basic Checks
- **trailing-whitespace**: Remove trailing whitespace
- **end-of-file-fixer**: Ensure files end with a newline
- **check-yaml/json/toml/xml**: Check file syntax
- **check-added-large-files**: Prevent committing large files (>10MB)
- **check-merge-conflict**: Check for merge conflict markers
- **debug-statements**: Check for debug statements (e.g., `pdb.set_trace()`)
- **mixed-line-ending**: Standardize line endings
- **check-case-conflict**: Prevent filename case conflicts

### Python Code Checks
- **ruff**: Code quality checking and auto-fix
- **ruff-format**: Code formatting (replaces black)

## Usage

### Automatic Installation (Recommended)
```bash
# Automatically install after cloning the project
uv sync  # hooks will be installed automatically
```

### Manual Installation
```bash
# Install pre-commit
uv add --dev pre-commit

# Install hooks
uv run pre-commit install
```

### Manual Check Execution
```bash
# Check all files
uv run pre-commit run --all-files

# Check specific files
uv run pre-commit run --files src/main.py

# Run only ruff check
uv run pre-commit run ruff --all-files
```

## Workflow

1. **Write Code** - Normal development
2. **Commit Code** - `git commit -m "your message"`
3. **Automatic Check** - pre-commit runs automatically
4. **If Issues Found** - Auto-fix or prompt for manual fix
5. **Re-commit** - Commit again after fixing

## How to Disable Pre-commit Hooks

### Method 1: Complete Uninstall (Not Recommended)
```bash
# Uninstall hooks
uv run pre-commit uninstall

# Reinstall
uv run pre-commit install
```

### Method 2: Skip Single Check
```bash
# Skip this check (use cautiously)
git commit --no-verify -m "urgent fix"
```

### Method 3: Disable Specific Checks
Edit `.pre-commit-config.yaml`, comment out unwanted hooks:

```yaml
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace
      # - id: debug-statements    # Comment out unwanted checks
```

### Method 4: Set Environment Variable
```bash
# Temporary disable
export SKIP=ruff,ruff-format
git commit -m "message"

# Or set in .env
echo "SKIP=ruff" >> .env
```

## Recommended Configurations

### Team Development (Recommended to Enable All)
Suitable for team projects requiring consistent code style.

### Personal Projects (Selective Enable)
```yaml
# Minimal configuration - only basic checks
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.8.0
    hooks:
      - id: ruff
        args: [--fix]
      - id: ruff-format
```

### Strict Mode (Uncomment Optional Checks)
Enable mypy type checking and bandit security checks.

## Frequently Asked Questions

### Q: Commits are very slow?
A: The first run downloads tools, subsequent runs will be fast. Use `--no-verify` for emergency commits.

### Q: Too many formatting changes?
A: Run `uv run pre-commit run --all-files` first to format all files at once.

### Q: Want to customize rules?
A: Edit ruff configuration in `pyproject.toml`:

```toml
[tool.ruff]
extend-ignore = ["E501"]  # Ignore line length check
```

### Q: How to use in CI/CD?
A: In GitHub Actions:

```yaml
- name: Run pre-commit
  run: |
    uv sync
    uv run pre-commit run --all-files
```

## Reference Resources

- [Pre-commit Official Documentation](https://pre-commit.com/)
- [Ruff Configuration Guide](https://docs.astral.sh/ruff/)
- [Project CLAUDE.md](../CLAUDE.md) - Complete Development Guide