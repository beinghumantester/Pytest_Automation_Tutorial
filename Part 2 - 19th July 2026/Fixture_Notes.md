# Pytest Fixtures - Detailed Notes

## What is a Fixture?

A fixture is one of the most powerful features provided by Pytest. It helps prepare everything that a test needs before execution and also performs cleanup after the test has finished.

Instead of writing the same setup code in every test, we can write it once inside a fixture and reuse it wherever required. This makes the test suite cleaner, easier to maintain, and reduces code duplication.

A fixture is created using the `@pytest.fixture` decorator.

Example:

```python
import pytest

@pytest.fixture
def browser():
    return "Chrome"

def test_launch(browser):
    assert browser == "Chrome"
```

In this example, the fixture returns the value `"Chrome"`, which is automatically passed to the test function.

---

# Why Do We Need Fixtures?

Imagine writing 100 Selenium test cases where every test needs to:

* Launch the browser
* Maximize the window
* Open the application
* Perform login

Without fixtures, the same code would be written in every test file. This increases duplication and makes maintenance difficult.

Using fixtures, the setup code is written only once and reused wherever required.

Some benefits of fixtures include:

* Reduces duplicate code
* Makes tests more readable
* Improves maintainability
* Encourages code reuse
* Supports setup and teardown
* Makes automation frameworks more organized

---

# How Does a Fixture Work?

The execution flow is simple:

1. Pytest identifies that a test requires a fixture.
2. The fixture executes first.
3. Any data returned by the fixture is passed to the test.
4. The test executes.
5. If the fixture contains cleanup code using `yield`, that cleanup executes after the test completes.

---

# Types of Fixtures

The following fixture types have been covered.

* Return Fixture
* Fixture Chaining
* Parameterized Fixture
* Scoped Fixture
* Autouse Fixture
* Fixtures using `conftest.py`

---

# 1. Return Fixture

A return fixture simply returns a value that can be used by one or more test cases.

It is the most basic type of fixture and is commonly used for providing test data.

Example:

```python
import pytest

@pytest.fixture
def user():
    return {
        "name": "Ujjwal",
        "role": "Tester"
    }

def test_user_name(user):
    assert user["name"] == "Ujjwal"

def test_user_role(user):
    assert user["role"] == "Tester"
```

### How it works

* The fixture executes first.
* It returns a dictionary.
* The returned dictionary is automatically injected into the test function.
* The same fixture can be reused by multiple test cases.

### Common Use Cases

* Test data
* URLs
* Login credentials
* Configuration values
* Static objects

---

# 2. Fixture Chaining

A fixture can use another fixture. This is known as fixture chaining or fixture dependency.

Instead of creating everything inside one fixture, multiple fixtures can work together.

Example:

```python
import pytest

@pytest.fixture
def username():
    return "Ujjwal"

@pytest.fixture
def greeting(username):
    return f"Hello {username}"

def test_message(greeting):
    assert greeting == "Hello Ujjwal"
```

### Execution Flow

```
username fixture
        ↓
greeting fixture
        ↓
test function
```

Pytest automatically understands that `greeting` depends on `username` and executes them in the correct order.

### Advantages

* Better code organization
* Higher reusability
* Easier maintenance
* Small fixtures with single responsibilities

### Real-world Example

In Selenium automation:

```
Database Connection
        ↓
User Details
        ↓
Browser Login
        ↓
Test Case
```

Each fixture performs one responsibility and passes its result to the next fixture.

---

# 3. Parameterized Fixture

Sometimes we want to execute the same test multiple times using different values.

Instead of writing multiple test cases, we can parameterize the fixture.

Example:

```python
import pytest

@pytest.fixture(params=["Chrome", "Firefox", "Edge"])
def browser(request):
    return request.param

def test_browser(browser):
    print(browser)
```

The test executes three times.

Execution:

```
Chrome
Firefox
Edge
```

### How it Works

Pytest stores each parameter inside `request.param`.

For every value:

* Fixture executes
* Test executes
* Next value is picked
* Test executes again

### Common Use Cases

* Multiple browsers
* Different environments
* User roles
* Multiple APIs
* Different test data

---

# 4. Scoped Fixture

By default, fixtures execute once for every test function.

Sometimes this is unnecessary.

Pytest allows controlling how long a fixture remains active using the `scope` parameter.

Available scopes are:

* function
* class
* module
* package
* session

---

## Function Scope

This is the default scope.

A new fixture instance is created for every test function.

```
Test 1

Create Fixture

↓

Execute Test

↓

Destroy Fixture

-------------------

Test 2

Create Fixture

↓

Execute Test

↓

Destroy Fixture
```

Best for independent test cases.

---

## Class Scope

The fixture is created once for all test methods inside a class.

```
Create Fixture

↓

Test 1

↓

Test 2

↓

Test 3

↓

Destroy Fixture
```

Useful when every test inside a class requires the same setup.

---

## Module Scope

The fixture is created once for an entire Python file.

```
Create Fixture

↓

All tests inside the file

↓

Destroy Fixture
```

Useful when connecting to a database or launching a browser only once for that module.

---

## Package Scope

The fixture remains active for all test modules inside a package.

Useful for large projects where multiple modules require the same setup.

---

## Session Scope

The fixture executes only once during the entire test session.

```
Start Testing

↓

Create Fixture

↓

Execute every test

↓

Destroy Fixture

↓

End Testing
```

This is commonly used for:

* Browser setup
* Database connection
* API authentication
* Global configuration

---

# 5. Autouse Fixture

Normally, fixtures are executed only when explicitly requested by a test.

Autouse fixtures execute automatically without being passed as parameters.

Example:

```python
import pytest

@pytest.fixture(autouse=True)
def before_each_test():
    print("Before Test")
    yield
    print("After Test")

def test_one():
    pass

def test_two():
    pass
```

Notice that neither test includes the fixture as an argument, yet it still runs before and after each test.

### When to Use

* Logging
* Screenshots
* Environment setup
* Database cleanup
* Browser cleanup
* Common initialization

### Advantages

* No need to call the fixture repeatedly.
* Keeps test cases clean.
* Ensures common setup always executes.

---

# 6. conftest.py Fixture

As projects grow, writing fixtures inside every test file becomes difficult.

Pytest solves this using a special file named `conftest.py`.

Fixtures defined inside `conftest.py` become automatically available to all test files within that directory (and its subdirectories) without importing them.

Example structure:

```
project/

├── conftest.py
├── test_login.py
└── test_dashboard.py
```

**conftest.py**

```python
import pytest

@pytest.fixture
def browser():
    return "Chrome"
```

**test_login.py**

```python
def test_login(browser):
    assert browser == "Chrome"
```

**test_dashboard.py**

```python
def test_dashboard(browser):
    assert browser == "Chrome"
```

Notice that neither test file imports the fixture. Pytest automatically discovers fixtures inside `conftest.py`.

### Advantages

* Centralized fixture management
* Eliminates duplicate code
* Improves project structure
* Makes fixtures reusable across multiple test files
* Simplifies maintenance

---

# Best Practices

* Keep fixtures focused on a single responsibility.
* Use meaningful fixture names.
* Prefer small, reusable fixtures over large ones.
* Store shared fixtures inside `conftest.py`.
* Choose the appropriate scope to avoid unnecessary setup and teardown.
* Use fixture chaining instead of repeating setup logic.
* Avoid using `autouse=True` unless every test genuinely requires the fixture.

---

# Summary

Fixtures are the foundation of Pytest. They help prepare test data, manage setup and cleanup, reduce duplicate code, and make test suites easier to maintain.

The fixture types covered are:

* **Return Fixture** – Returns reusable data for tests.
* **Fixture Chaining** – Allows one fixture to depend on another.
* **Parameterized Fixture** – Executes the same test with multiple inputs.
* **Scoped Fixture** – Controls how long a fixture remains active.
* **Autouse Fixture** – Executes automatically without being requested.
* **conftest.py Fixture** – Shares fixtures across multiple test files without explicit imports.

Understanding these concepts provides a strong foundation for building scalable and maintainable Pytest automation frameworks.
