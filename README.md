# GridOps

A simple Python library for grid operations.

## Prerequisites

- Python 3.8 or higher
- pip (comes with Python)

## Virtual Environment Setup

### Why Use Virtual Environments?

A virtual environment keeps your project dependencies isolated from your system Python. This prevents conflicts between different projects and ensures reproducible builds.

### Creating and Using Virtual Environment

```bash
# Navigate to your project directory
cd GridOps

# Create virtual environment
python -m venv venv

# Activate it
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

**Note**: You'll see `(venv)` in your terminal prompt when the virtual environment is active.

### Installing the Project

```bash
# Install the package with development tools
pip install -e ".[dev]"

# Or if you also want editor support (LSP, code completion):
pip install -e ".[dev,editor]"
```

**What does `pip install -e .` do?**
- `-e` = "editable" mode - changes to your code take effect immediately
- `.` = install the current directory as a package
- `[dev]` = also install development dependencies (testing, linting, etc.)

## Understanding pyproject.toml

The `pyproject.toml` file is the modern way to configure Python packages. It replaces the old `setup.py` approach.

**Key sections:**

```toml
[project]
name = "GridOps"                    # Package name
dependencies = []                   # Runtime dependencies (what users need)

[project.optional-dependencies]
dev = ["ruff", "black", "pytest"]  # Development tools (what developers need)

[tool.hatch.build.targets.wheel]
packages = ["src/gridops"]          # Tells pip where your code is
```

**Why use pyproject.toml?**
- Modern standard (PEP 621)
- One file for all configuration
- Better tool integration
- Automatic dependency management

### Development Workflow

#### Running Tests
```bash
pytest                    # Run all tests
pytest tests/test_core.py # Run specific test file
pytest -v                # Verbose output
```

#### Code Quality
```bash
# Format code
black src/ tests/

# Lint code (check for errors and style)
ruff check src/ tests/

# Fix auto-fixable issues
ruff check src/ tests/ --fix

# Type checking
mypy src/
```

#### Adding Dependencies

**For users of your library:**
```toml
# In pyproject.toml [project] section
dependencies = [
    "requests>=2.25.0",
    "numpy>=1.20.0",
]
```

**For development only:**
```toml
# In [project.optional-dependencies] section
dev = [
    "ruff>=0.3.0",
    "pytest>=8.0.0",
    # ... other dev tools
]
```

After editing `pyproject.toml`, reinstall:
```bash
pip install -e ".[dev]"
```

### Deactivating Virtual Environment

When you're done working:
```bash
deactivate
```

This returns you to your system Python environment.
