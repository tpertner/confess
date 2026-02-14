# Contributing to Honesty Harness

Thanks for your interest in improving this project.

## Ways to contribute

### 1) Add a new test case

If you've found a failure mode that isn't covered:

- Add it to `testsuites/mini_suite.yaml`
- Include a clear description in the `notes` field
- Set appropriate severity (5 = critical, 4 = high, 3 = medium)
- Test it locally before submitting

### 2) Improve docs

Documentation improvements are always welcome, especially:

- Clarifying confusing sections
- Adding real-world examples
- Fixing typos or broken links

### 3) Report a bug

Open an issue with:

- steps to reproduce
- expected vs actual behavior
- your environment (Python version, model, OS)

## Submitting changes

1. Fork the repo
2. Create a branch: `git checkout -b feature/your-feature`
3. Make your changes
4. Run linters locally (optional but recommended)
5. Push and open a pull request

## Code style

- Follow existing patterns in the codebase
- Keep test cases focused (one failure mode per test)
- Write clear constraint names and descriptions
- Add comments for non-obvious logic

## Questions?

Open an issue or reach out to Tracy Pertner (Tray).
