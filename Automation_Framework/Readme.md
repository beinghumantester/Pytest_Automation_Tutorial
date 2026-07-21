# Pytest Automation Framework from Scratch

A step-by-step learning repository that demonstrates how to build a Selenium + Pytest automation framework from the ground up.

Unlike repositories that provide a finished framework, this project focuses on **understanding why each component exists** and **how an automation framework evolves over time**.

Whether you're new to Pytest, preparing for automation interviews, or looking to strengthen your framework design skills, this repository is designed to help you learn by building.

---

# What You'll Learn

Throughout this series, you'll learn how to build an automation framework by implementing one concept at a time.

Topics include:

* Python fundamentals required for automation
* Pytest basics
* Test discovery
* Assertions
* Fixtures
* Fixture scopes
* Parameterized fixtures
* Yield fixtures
* Factory fixtures
* `conftest.py`
* Selenium WebDriver integration
* Cross-browser execution
* Page Object Model (POM)
* Configuration management
* Test data management
* HTML Reports
* Logging
* Screenshots on failure
* Hooks
* Parallel execution
* CI/CD integration
* Best practices for scalable automation frameworks

---

# Tech Stack

* Python
* Pytest
* Selenium WebDriver
* Pytest HTML
* Faker
* WebDriver Manager

---

# Project Structure

```text
AutomationFramework/
│
├── config/
│   └── config.py
│
├── pages/
│   └── login_page.py
│
├── reports/
│
├── screenshots/
│
├── test_data/
│
├── tests/
│   └── test_login.py
│
├── utils/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

# Getting Started

## 1. Clone the Repository

```bash
git clone <repository-url>
```

```bash
cd <repository-folder>
```

---

## 2. Create a Virtual Environment

Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv
```

Activate

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Run Tests

Run all tests

```bash
pytest
```

Verbose output

```bash
pytest -v
```

Generate HTML Report

```bash
pytest --html=reports/report.html
```

---

# Current Features

* Selenium with Pytest
* Browser fixtures
* Cross-browser execution
* Shared fixtures using `conftest.py`
* Organized project structure
* Configuration management
* Page Object Model
* HTML Reports

The framework will continue to evolve with every new episode.

---

# Learning Roadmap

* [x] Pytest Introduction
* [x] Assertions
* [x] Fixtures
* [x] Yield Fixtures
* [x] Parameterized Fixtures
* [x] Factory Fixtures
* [x] `conftest.py`
* [x] Selenium Integration
* [x] Framework Structure
* [ ] Page Object Model
* [ ] Configuration File
* [ ] HTML Reports
* [ ] Logging
* [ ] Utilities
* [ ] Test Data Management
* [ ] Screenshots on Failure
* [ ] Hooks
* [ ] Parallel Execution
* [ ] Data-Driven Testing
* [ ] CI/CD Integration
* [ ] Docker
* [ ] GitHub Actions

---

# Why This Repository?

Many automation repositories showcase a complete framework but don't explain the reasoning behind its architecture.

This repository takes a different approach by building the framework incrementally. Each addition is introduced only when it solves a real problem, making it easier to understand the purpose and practical use of every component.

---

# YouTube Series

This repository accompanies the **Pytest Automation Framework from Scratch** YouTube series.

Each video builds on the previous one, allowing you to follow along and implement the framework yourself.

---

# Contributing

Contributions are welcome.

If you find a bug, have an improvement, or would like to add a feature, feel free to open an issue or submit a pull request.

---

# Support

If this repository helps you learn something new:

*  Star the repository
*  Fork it
*  Follow the YouTube series
*  Connect on LinkedIn
*  Share it with other testers

---

# License

This project is licensed under the MIT License.

---

Happy Testing! 🚀
