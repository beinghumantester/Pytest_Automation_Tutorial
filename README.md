# Pytest Learning Repository

Welcome! 

This repository contains all the source code used throughout my Pytest learning series. The goal of this repository is not just to show the final code but to help understand **why** each concept exists and **how** it is used in real projects.

Whether you're just getting started with Pytest or looking to strengthen your automation testing skills, you can use these examples to learn, practice, and experiment.

---

## What You will Learn

This repository covers the core concepts of Pytest step by step.

### Fixtures

* Return Fixture
* Yield Fixture
* Fixture Chaining
* Parameterized Fixture
* Scoped Fixture
* Autouse Fixture
* Factory Fixture
* Sharing Fixtures using `conftest.py`

### Pytest Basics

* Writing Test Cases
* Assertions
* Test Discovery
* Running Tests
* Naming Conventions

### Advanced Topics *(Coming Soon)*

* Markers
* Parametrize
* Hooks
* Custom Command Line Options
* Logging
* HTML Reports
* Screenshots
* Page Object Model (POM)
* Selenium Integration
* Data-Driven Testing
* Faker
* Parallel Execution
* CI/CD Integration
* Best Practices
* Production-Ready Framework

---

## Repository Structure

```text
.
├── fixtures/
├── basics/
├── hooks/
├── reports/
├── pom/
├── utils/
├── test_data/
├── screenshots/
├── conftest.py
├── requirements.txt
└── README.md
```

> The repository will continue to grow as new videos are published.

---

## Prerequisites

Before running the examples, make sure you have:

* Python 3.10 or later
* Pytest installed
* A code editor such as VS Code

---

## Installation

Clone the repository:

```bash
git clone https://github.com/beinghumantester/Pytest_Automation_Tutorial.git
```

Move into the project directory:

```bash
cd https://github.com/beinghumantester/Pytest_Automation_Tutorial.git
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Tests

Run all tests:

```bash
pytest
```

Run tests with verbose output:

```bash
pytest -v
```

Run tests and display print statements:

```bash
pytest -s
```

Run tests with both verbose output and print statements:

```bash
pytest -s -v
```

Run a specific file:

```bash
pytest test_file.py
```

Run a specific test:

```bash
pytest test_file.py::test_name
```

---

## Who Is This Repository For?

This repository is useful for:

* Beginners learning Pytest
* Manual Testers moving into Automation
* QA Engineers
* SDETs
* Anyone preparing for automation testing interviews

---

## Learning Approach

Every example in this repository follows the same pattern:

1. Understand the problem.
2. Learn the Pytest feature.
3. Write the code.
4. Execute the test.
5. Understand the output.
6. Connect the concept to real-world automation frameworks.

The focus is on understanding the concepts rather than memorizing syntax.

---

## Contributions

If you find an issue, have suggestions, or want to improve an example, feel free to open an issue or submit a pull request.

Constructive feedback is always welcome.

---

## Connect With Me

If these examples help you learn something new, consider connecting with me.

* LinkedIn: *([Linkedin profile link](https://www.linkedin.com/in/beinghumantester/))*
* YouTube: *([Youtube channel link](https://www.youtube.com/@beinghumantester/))*
* GitHub: *[(GitHub profile)](https://github.com/beinghumantester)*

---

Keep Learning and Keep Growing! 

