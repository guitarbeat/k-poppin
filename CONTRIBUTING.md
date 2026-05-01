# Contributing

Thank you for your interest in contributing to this project! We Acpreciate your effort and want to make the process as smooth as possible.

## Development Setup

### Prerequisites
- Node.js (v18 or higher)
- npm or yarn

### Getting Started

1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/your-username/repo-name.git
   cd repo-name
   ```
3. Install dependencies:
   ```bash
   npm install
   ```

## Linting and Code Standards

We maintain consistent code quality using ESLint and Prettier.

### Running Linter
```bash
npm run lint
```

### Auto-formatting Code
```bash
npm run format
```

Pre-commit hooks automatically run linting on staged files.

## Testing

Before submitting a pull request, ensure all tests pass:

```bash
npm test
```

## Making a Pull Request

1. Create a feature branch:
   ```bash
   git checkout -b feat/my-feature
   ```
2. Make your changes and commit them:
   ```bash
   git add .
   git commit -m "feat: add my feature"
   ```
3. Push to your fork:
   ```bash
   git push origin feat/my-feature
   ```
4. Open a Pull Request with a clear description of your changes

## Code Style

- Follow the Airbnb JavaScript style guide (enforced by ESLint)
- Use Prettier for automatic code formatting
- Write meaningful commit messages
- Include comments for complex logic

## Pull Request Guidelines

- Keep PRs focused on a single feature or fix
- Write descriptive PR titles and descriptions
- Ensure CI/CD checks pass
- Request review from maintainers
- Be responsive to feedback

## Questions?

Feel free to open an issue for questions or discussions.