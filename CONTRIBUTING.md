# Contributing

## Development Setup

1.  Clone the repository.
2.  Install Node.js dependencies:
    ```bash
    npm install
    ```
3.  Install Python dependencies:
    ```bash
    pip install -r requirements.txt # if exists, otherwise:
    pip install ruff black playwright
    playwright install chromium
    ```

## Linting & Formatting

We use **ESLint** and **Prettier** for JavaScript, and **Ruff** and **Black** for Python.

### JavaScript
- Lint: `npm run lint`
- Fix Lint: `npm run lint:fix`
- Format Check: `npm run format:check`
- Format Write: `npm run format`

### Python
- Lint: `ruff check .`
- Format: `black .`

## Testing

Run the validation script to check `songs.json`:
```bash
python scripts/validate_songs.py
```

Run frontend verification (requires local server):
```bash
python -m http.server 8000 &
export BASE_URL=http://localhost:8000
python verification/verify_load.py
```

## Pre-commit Hooks

We use `pre-commit` to ensure code quality.
Install pre-commit:
```bash
pip install pre-commit
pre-commit install
```
