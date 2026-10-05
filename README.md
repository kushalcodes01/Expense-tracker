# Expense Tracker API

A RESTful Expense Tracker API built using **Python, Flask, and SQLite**. This project allows users to create, view, update, and delete expenses through API endpoints while maintaining data integrity through input validation.

## Features

### Expense Management

* Add new expenses
* View all expenses
* View a specific expense by ID
* Update existing expenses
* Delete expenses

### Validation

* Prevent empty titles
* Prevent empty categories
* Prevent empty dates
* Prevent negative or zero amounts
* Proper error handling for non-existing expense IDs

## Technologies Used

* Python 3
* Flask
* SQLite
* Postman
* Git & GitHub

## Project Structure

```text
Expense_tracker/
│
├── main.py
├── dbase.py
├── requirements.txt
├── README.md
├── .gitignore
└── expense.db
```

## API Endpoints

### Create Expense

```http
POST /expenses
```

Request Body:

```json
{
  "title": "Pizza",
  "amount": 250,
  "category": "Food",
  "date": "2026-10-05"
}
```

### Get All Expenses

```http
GET /expenses
```

### Get Expense By ID

```http
GET /expenses/<id>
```

### Update Expense

```http
PUT /expenses/<id>
```

### Delete Expense

```http
DELETE /expenses/<id>
```

## Installation

Clone the repository:

```bash
git clone https://github.com/kushalcodes01/Expense-tracker.git
```

Move into the project directory:

```bash
cd Expense-tracker
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

Run the application:

```bash
python main.py
```

## Learning Outcomes

Through this project, I learned:

* REST API fundamentals
* CRUD operations
* Flask routing
* SQLite database integration
* Input validation
* HTTP methods (GET, POST, PUT, DELETE)
* Postman API testing
* Git and GitHub workflow

## Future Improvements

* Category-wise expense reports
* Monthly expense summaries
* User authentication
* PostgreSQL integration
* Deployment on Render

## Author

Kushal Lamsal

GitHub: https://github.com/kushalcodes01
LinkedIn: https://linkedin.com/in/kushallamsal1
