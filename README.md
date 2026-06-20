# SauceDemo Test Automation Suite

## Overview

This project contains an automated regression test suite for the SauceDemo web application:

https://www.saucedemo.com/

The framework is implemented using Python, Playwright and Pytest following the Page Object Model (POM) design pattern.

The goal of this project is to verify the core functionalities of the application through automated end-to-end tests.

---

## Technologies

* Python 3.10.5
* Playwright
* Pytest
* Pytest-HTML
* Git

---

## Framework Features

* Page Object Model (POM)
* Automated UI testing using Playwright
* Data-driven login tests using Pytest parameterization
* Automated HTML report generation
* Regression test coverage for critical user workflows

---

## Project Structure

```text
.
├── pages/
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── tests/
│   ├── test_login.py
│   ├── test_inventory.py
│   ├── test_cart.py
│   ├── test_checkout.py
│   └── test_logout.py
│
├── utils/
│   └── test_data.py
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Test Coverage

### Login

* Valid login (for multiple SauceDemo user types)
* Invalid login
* Locked-out user validation

### Inventory

* Inventory page loading
* Product count validation
* Product name validation
* Product price validation
* Product sorting validation by Price low to high
* Product sorting validation by name a to z

### Cart

* Add product to cart
* Remove product from cart
* Cart badge validation
* Cart content validation

### Checkout

* Successful checkout
* Missing first name validation
* Missing last name validation
* Missing postal code validation

### Logout

* Successful logout

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd <repository-name>
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install Playwright browsers:

```bash
playwright install
```

---

## Running Tests

Run all tests:

```bash
pytest
```

The test suite automatically generates an HTML report after execution.

---

## HTML Report

After the test run, the report can be found at:

```text
reports/report.html
```

Open the report:

```bash
start reports\report.html
```

---

## Design Approach

The framework follows the Page Object Model (POM) design pattern.

Page interactions are separated from test logic to improve:

* Readability
* Maintainability
* Reusability

This approach makes the framework easier to scale and maintain as new tests are added.

---

## Assumptions

* Tests are executed against the public SauceDemo environment.
* Product data and product count are based on the current state of the application.
---

## Author

Hamza Salaar
