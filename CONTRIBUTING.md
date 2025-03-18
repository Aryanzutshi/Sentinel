# Contributing to Sentinel

Thank you for your interest in contributing to the Smart Contract Analyzer! We welcome contributions from the community to help improve this tool.

## How to Contribute

### 1. Reporting Issues
If you find a bug or have a feature request, please open an issue on GitHub:
- Provide a clear and descriptive title.
- Include steps to reproduce the issue (if applicable).
- Add relevant code snippets, logs, or screenshots.

### 2. Submitting Pull Requests
We welcome pull requests (PRs) for bug fixes, new features, or improvements. Follow these steps:

1. **Fork the Repository**: Create a fork of the repository on GitHub.
2. **Create a Branch**: Use a descriptive branch name (e.g., `fix/reentrancy-detection`).
3. **Make Changes**: Implement your changes and ensure they follow the project's coding style.
4. **Test Your Changes**: Run the existing tests and add new tests if applicable.
5. **Submit a PR**: Open a pull request against the `main` branch.

### 3. Coding Guidelines
- Follow the [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide for Python code.
- Write clear and concise commit messages.
- Document new features or changes in the `README.md` file.

### 4. Adding New Vulnerability Patterns
To add new vulnerability patterns:
1. Edit the `vulnerabilities.json` file.
2. Add a new entry with the following format:
   ```json
   {
       "name": "Vulnerability Name",
       "pattern": "Regex Pattern"
   }