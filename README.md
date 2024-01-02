**Weather API Testing Project**

Description

This project contains automated tests for validating weather data fetched from
the OpenWeatherMap API. It includes tests for current weather data as well as forecasts,
ensuring the accuracy and reliability of the data provided by the API.

**Getting Started**

Dependencies
Python 3.x
requests - library for making API calls
pytest - for running the tests

Installing
Clone this repository or download the source code.

Install required packages: pip install requests pytest

Setting Up

Sign up for an API key from OpenWeatherMap.

Add the API key to your environment variables or a configuration file.

Executing Tests

Run the tests using pytest -> pytest test_weather.py

**Writing Tests**

The test_weather.py file contains automated tests for the OpenWeatherMap API.
It includes a WeatherApiClient class for handling API requests and utility functions for fetching and validating weather data.

Key Components

1.WeatherApiClient: A class to interact with the OpenWeatherMap API.

2.Test functions: Functions prefixed with test_ that use pytest assertions to validate
API responses.

**Conversion Testing Project UI**

**Setup**
install python
install selenium 4.16
install requests
install pytest
install webdriver-manager
install allure

Description

This project contains a Python script, test_conversions.py, designed to perform
automated testing of conversion functionalities. It implements the Page Object Model
(POM) design pattern to provide an efficient and maintainable test structure.

Page Object Model (POM)
The Page Object Model is a test automation design pattern that encapsulates the
representation of application pages/sections in the test code.
This model helps to make the test code more readable, maintainable, and reusable.

**Key Benefits**

Maintainability ->Changes in the UI can be updated in one place rather than in all tests.
Readability ->Makes the test code more concise and easier to understand.
Reusability ->Common page elements and functionalities can be reused across multiple test scripts.

Object-Oriented Programming (OOP)

Object-Oriented Programming (OOP) is a programming paradigm based on the concept of "objects",
which are data structures containing data, in the form of fields, often known as attributes; and code,
in the form of procedures, often known as methods.

Key Principles of OOP

Encapsulation: Bundling the data and methods that operate on the data within one unit (e.g., a class in Python).
This hides the internal state of the object from the outside.
Abstraction: Abstracting away complex implementations and showing only the necessary features of an object.
This helps reduce complexity and increase efficiency.
Inheritance: Allowing a new class to inherit properties and methods from an existing class.
This promotes code reusability.
Polymorphism: Letting a single function or method behave differently based on the 
object or parameters it is working with.

Implementation in This Project

In test_conversions.py, OOP principles are used to structure the tests efficiently.
Classes represent different components or functionalities being tested, with methods encapsulating specific test actions or sequences. This approach enhances code readability, maintainability, and scalability.