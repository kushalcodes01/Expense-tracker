from flask import Flask, request, jsonify
from dbase import (
    create_table,
    add_expense,
    get_all_expenses,
    get_expense_by_id,
    update_expense,
    delete_expense,
    get_expenses_by_category,
    get_total_expense,
    get_category_summary,
    get_expenses_by_date,
    get_expenses_by_month
)

app = Flask(__name__)

create_table()

@app.route("/")
def home():
    return "Expense Tracker API runnning"

@app.route("/expenses" ,methods=["POST"])
def create_expense():

    data = request.get_json()

    title = data["title"]
    amount = data["amount"]
    category = data["category"]
    date = data["date"]

    if not title.strip():
        return jsonify({
            "message": "Title cannot be empty"
        }), 400

    if amount<= 0:
        return jsonify({
            "message": "Amount must be greater than 0"
        }), 400

    if not category.strip():
        return jsonify({
            "message": "Category cannot be empty"
        }), 400

    if not date.strip():
        return jsonify({
            "message" : "Date cannot be empty"
        }), 400

    add_expense(title, amount, category, date)

    return jsonify({
        "message": "Expense added successfully"
    }), 201

@app.route("/expenses", methods=["GET"])
def get_expenses():

    expenses = get_all_expenses()

    return jsonify(expenses), 200

@app.route("/expenses/<int:expense_id>", methods=["GET"])
def get_expense(expense_id):

    expense = get_expense_by_id(expense_id)

    if expense:
        return jsonify(expense), 200

    return jsonify({
        "message": "Expense not found"
    }), 404

@app.route("/expenses/<int:expense_id>", methods=["PUT"])
def edit_expense(expense_id):

    data = request.get_json()

    title = data["title"]
    amount = data["amount"]
    category = data["category"]
    date = data["date"]

    if not title.strip():
        return jsonify({
            "message": "Title cannot be empty"
        }), 400

    if amount<= 0:
        return jsonify({
            "message" : "Amount must be greater than 0"
        }), 400

    if not category.strip():
        return jsonify({
            "message": "Category cannot be empty"
        }), 400

    if not date.strip():
        return jsonify({
            "message": "Date cannot be empty"
        }), 400

    updated = update_expense(
            expense_id,
            title,
            amount,
            category,
            date
    )

    if updated == 0:
        return jsonify({
        "message": "Expense not found"
        }), 404

    return jsonify({
        "message": "Updated Successfully"
    }), 200
    
@app.route("/expenses/<int:expense_id>", methods=["DELETE"])
def remove_expense(expense_id):

    deleted = delete_expense(expense_id)

    if deleted == 0:
        return jsonify({
            "message" : "Expense not found"
        }), 404

    return jsonify({
        "message":"Expense Deleted successfully"
    }), 200

@app.route("/expenses/category/<category>", methods=["GET"])
def expenses_by_category(category):

    expenses = get_expenses_by_category(category)

    if not expenses:
        return jsonify({
            "message": "No Expenses found for this category"
        }), 404

    return jsonify(expenses), 200

@app.route("/expenses/total", methods=["GET"])
def total_expenses():

    total = get_total_expense()

    return jsonify({
        "total expense": total
    }), 200

@app.route("/expenses/summary/category", methods=["GET"])
def category_summary():

    summary = get_category_summary()

    result = {}

    for category, total in summary:
        result[category] = total

    return jsonify(result), 200


@app.route("/expenses/date/<date>", methods=["GET"])
def expenses_by_date(date):

    expenses = get_expenses_by_date(date)

    if not expenses:
        return jsonify({
            "message": "No expenses for this date"
        }), 404

    return jsonify(expenses), 200


@app.route("/expenses/month/<month>", methods=["GET"])
def expenses_by_month(month):

    expenses = get_expenses_by_month(month)

    if not expenses:
        return jsonify({
            "message": "No expenses for this month"
        }), 404

    return jsonify(expenses), 200


if __name__ == "__main__":
    app.run(debug=True)