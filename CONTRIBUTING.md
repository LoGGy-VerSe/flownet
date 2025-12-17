# Contributing to FlowNet

Thank you for considering contributing to FlowNet! This document outlines the process and guidelines for contributing.

## Code of Conduct

This project adheres to a Code of Conduct that all contributors are expected to follow. Please read [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) before contributing.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates. When creating a bug report, include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps to reproduce the problem**
- **Provide specific examples** (configuration files, commands used, etc.)
- **Describe the behavior you observed** and what behavior you expected
- **Include Terraform version** and any relevant environment details

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion:

- **Use a clear and descriptive title**
- **Provide a detailed description of the suggested enhancement**
- **Explain why this enhancement would be useful**
- **List any similar features in other projects** if applicable

### Pull Requests

1. **Fork the repository** and create your branch from `main`
2. **Follow the coding standards** used throughout the project
3. **Write clear commit messages** following conventional commits format:
   - `feat:` for new features
   - `fix:` for bug fixes
   - `docs:` for documentation changes
   - `refactor:` for code refactoring
   - `test:` for adding tests
   - `chore:` for maintenance tasks

4. **Test your changes**:
   - Run `terraform fmt` to format your code
   - Run `terraform validate` to validate syntax
   - Run `terraform plan` to ensure it works as expected

5. **Update documentation** as needed
6. **Submit the pull request** with a clear description of the changes

## Development Setup

1. Clone your fork:
```bash
git clone https://github.com/YOUR-USERNAME/flownet.git
cd flownet
```

2. Install Terraform (if not already installed):
```bash
# Follow instructions at https://www.terraform.io/downloads
```

3. Initialize the project:
```bash
terraform init
```

## Coding Standards

### Terraform Style Guide

- Use consistent naming conventions (snake_case for resources)
- Add descriptions to all variables and outputs
- Use modules for reusable components
- Keep files organized (separate variables, outputs, main logic)
- Use meaningful resource names
- Comment complex logic

### File Organization

- `main.tf` - Primary resource definitions
- `variables.tf` - Input variable declarations
- `outputs.tf` - Output value declarations
- `versions.tf` - Terraform and provider version constraints
- `locals.tf` - Local value definitions (if needed)

### Documentation

- Update README.md if adding new features
- Add inline comments for complex logic
- Update CHANGELOG.md following [Keep a Changelog](https://keepachangelog.com/) format

## Testing

Before submitting a pull request:

```bash
# Format code
terraform fmt -recursive

# Validate configuration
terraform validate

# Check formatting
terraform fmt -check -recursive

# Generate and review plan
terraform plan
```

## Review Process

1. All pull requests require at least one review
2. CI/CD checks must pass
3. Code must follow style guidelines
4. Documentation must be updated
5. No merge conflicts with main branch

## Questions?

Feel free to open an issue for any questions or clarifications needed.

Thank you for your contributions!
