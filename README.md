# Expense Tracker API

A RESTful Expense Tracker API built using **Python, Flask, and SQLite**. This project allows users to create, manage, filter, and analyze expenses through API endpoints while maintaining data integrity through validation.

---

## Features

### Expense Management

* Add new expenses
* View all expenses
* View a specific expense by ID
* Update existing expenses
* Delete expenses

### Filters

* Filter expenses by category
* Filter expenses by date
* Filter expenses by month

### Analytics

* Calculate total expenses
* Category-wise expense summary

### Validation

* Prevent empty titles
* Prevent empty categories
* Prevent empty dates
* Prevent negative or zero amounts
* Proper handling of non-existing expense IDs

---

## Technologies Used

* Python 3
* Flask
* SQLite
* Postman
* Git
* GitHub

---

## Project Structure

```text
Expense_tracker/
│
├── main.py
├── dbase.py
├── expense.db
├── requirements.txt
├── README.md
└── .gitignore
```

---

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
    "date": "2026-10-06"
}
```

---

### Get All Expenses

```http
GET /expenses
```

---

### Get Expense By ID

```http
GET /expenses/<id>
```

---

###
