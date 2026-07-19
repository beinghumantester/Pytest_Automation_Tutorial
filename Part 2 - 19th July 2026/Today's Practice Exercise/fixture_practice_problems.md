# Pytest Fixtures - Practice Problems

These exercises are designed to help you strengthen your understanding of Pytest fixtures. Try solving them on your own before looking for solutions.

---

#  Level 1 - Return Fixture

## Problem 1 - Student Information

Create a fixture that returns the following dictionary:

```python
{
    "name": "Rahul",
    "age": 21,
    "course": "B.Tech"
}
```

Write test cases to verify:

* Student name
* Student age
* Student course

---

## Problem 2 - Shopping Cart

Create a fixture that returns:

```python
["Laptop", "Mouse", "Keyboard"]
```

Write test cases to verify:

* Laptop exists in the cart.
* Total number of items is 3.

---

## Problem 3 - Employee Details

Create a fixture that returns employee information.

Example:

```python
{
    "id": 101,
    "name": "John",
    "department": "QA",
    "salary": 60000
}
```

Write test cases to verify:

* Employee ID
* Department
* Salary

---

#  Level 2 - Fixture Chaining

## Problem 4 - Company and Employee

Create two fixtures:

```text
company()
    ↓
employee()
```

The `employee()` fixture should use the `company()` fixture.

Expected Output:

```text
Rahul works at Google
```

---

## Problem 5 - Customer Address

Create the following fixture dependency:

```text
city()
    ↓
address()
    ↓
customer()
```

Verify the final customer details.

---

## Problem 6 - Login System

Create three fixtures:

```text
database()
    ↓
user()
    ↓
login()
```

The `login()` fixture should depend on the previous two fixtures.

Write a test to verify the login message.

---

#  Level 3 - Parameterized Fixture

## Problem 7 - Browser Testing

Run the same test for:

* Chrome
* Firefox
* Edge

Print the browser name during execution.

---

## Problem 8 - Numbers

Parameterize the fixture with:

```text
5
10
15
20
```

Verify that every number is greater than zero.

---

## Problem 9 - User Roles

Parameterize the fixture with:

* Admin
* Tester
* Developer

Print a welcome message for each role.

---

#  Level 4 - Scoped Fixture

## Problem 10 - Module Scope

Create a module-scoped fixture.

Print:

```text
Connecting Database
```

Execute three test cases.

Observe how many times the fixture executes.

---

## Problem 11 - Function Scope

Create a function-scoped fixture.

Print:

```text
Launching Browser
```

Create three test cases.

Observe the execution count.

---

## Problem 12 - Session Scope

Create a session-scoped fixture.

Print:

```text
Application Started
```

Execute multiple test cases.

Observe the execution behavior.

---

#  Level 5 - Autouse Fixture

## Problem 13 - Automatic Setup

Create an autouse fixture that prints:

```text
Before Test
```

before every test and

```text
After Test
```

after every test.

Create four test cases.

Notice that the fixture is never passed as a parameter.

---

## Problem 14 - Test Counter

Create an autouse fixture that increases a counter before every test.

Print the counter value inside each test.

---

## Problem 15 - Logging

Create an autouse fixture that prints:

```text
Test Started
```

before every test and

```text
Test Finished
```

after every test.

---

#  Level 6 - conftest.py

## Problem 16 - Browser Fixture

Move the following fixture into `conftest.py`.

```python
browser()
```

Use it inside:

* `test_login.py`
* `test_dashboard.py`
* `test_profile.py`

without importing the fixture.

---

## Problem 17 - Base URL

Create a fixture named `base_url()` inside `conftest.py`.

Use it in multiple test files.

---

## Problem 18 - Credentials

Create a fixture named `credentials()` inside `conftest.py`.

Use it across three different test modules without importing it.

---

#  Mini Challenges

## Challenge 1

Create the following fixture chain:

```text
database()
    ↓
employee()
```

Parameterize the employee test so that it executes on:

* Chrome
* Firefox
* Edge

---

## Challenge 2

Create a program using:

* Module Scope
* Autouse Fixture
* Return Fixture

Observe the execution order.

---

## Challenge 3

Move the following fixtures into `conftest.py`:

* Browser
* Login Credentials
* Base URL

Use them across multiple test files.

---

#  Real-World Challenge

Imagine you're testing an e-commerce application.

Requirements:

* Create a fixture for the base URL.
* Create a fixture for login credentials.
* Create a fixture for product data.
* Launch the browser only once per module.
* Log every test automatically.
* Store common fixtures inside `conftest.py`.

Write test cases for:

* Login
* Search Product
* Add to Cart
* Checkout

---

#  Concept Check

Answer the following questions without writing code.

1. Which fixture type is used to provide reusable data to tests?
2. What is fixture chaining?
3. Why would you use a parameterized fixture?
4. What is the default fixture scope in Pytest?
5. When would you choose `module` scope instead of `function` scope?
6. What is the purpose of an autouse fixture?
7. Why is `conftest.py` used?
8. Do fixtures defined in `conftest.py` need to be imported?
9. Can one fixture depend on another fixture?
10. Which fixture scope executes only once during the entire test session?

---


