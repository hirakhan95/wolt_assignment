# Delivery Fee Calculator API

## Overview
This project is an implementation of an API that calculates the delivery fee based on cart value, delivery distance, number of items, and order time. It follows specified rules for calculating fees, including surcharges and rush hour rates.

## Requirements
- Python 3.7 or higher
- Django 3.x
- Django REST Framework
- [dateutil](https://pypi.org/project/python-dateutil/) package
- [pytest](https://pypi.org/project/pytest/) for running tests

## Installation & Running the Project
To run this project after unzipping the provided archive, follow these steps:

1. Navigate to the project directory:
   ```bash
   cd path_to_unzipped_folder 
   ```
   
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   
4. Navigate to the Django project directory (where manage.py is located) and run:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
   
5. Run the Development Server
   
   ```bash
   python manage.py runserver
   ```
   
The API will be available at http://localhost:8000/


## Using the API

A Postman collection is provided in the `postman` folder in this project.

### Steps to Use the API via Postman:
1. Open Postman and import the collection from the project's `postman` folder into your Postman workspace.
2. The imported collection includes the API endpoint and sample parameters used for testing.
3. Send a POST request to the endpoint with the required JSON payload. The endpoint URL is `http://localhost:8000/api/`


## Running Tests

To run tests, execute:

   ```bash
   pytest
   ```