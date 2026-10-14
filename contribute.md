# Contributing

Thanks for your interest in contributing to Moonlit Map Adventure!

## Getting Started

1. Fork the repository and clone your fork.
2. Make sure Python 3.10 or newer is installed.
3. Create a branch for your change:

   ```bash
   git checkout -b describe-your-change
   ```

This project has no external dependencies, so no package installation is required.

## Making Changes

- Keep the game easy to read and play from the command line.
- Follow the existing Python style and naming conventions.
- Preserve the branching adventure structure when adding scenes or endings.
- Include or update tests for behavior you change when practical.
- Keep changes focused on the purpose of your branch.

## Running Checks Locally

Run the same syntax check used by CI:

```bash
python3 -m compileall -q .
```

If tests are present, run them with:

```bash
python3 -m unittest discover --start-directory . --pattern "test*.py" --verbose
```

You can play the game locally with:

```bash
python3 adventure.py
```

## Pull Requests

Before opening a pull request:

- Confirm the game starts and the changed paths work as expected.
- Run the relevant checks locally.
- Write a clear description of what changed and why.
- Keep commits and pull requests focused.

GitHub Actions runs the CI workflow automatically for pushes and pull requests.

## Reporting Issues

When reporting a bug, include:

- A clear description of the problem.
- The steps needed to reproduce it.
- The Python version and operating system.
- The expected and actual behavior.

