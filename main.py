from flask import Flask, request, jsonify
from dbase import create_table, add_expense, get_all_expenses

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

    add_expense(title, amount, category, date)

    return jsonify({
        "message": "Expense added successfully"
    }), 201

@app.route("/expenses", methods=["GET"])
def get_expenses():

    expenses = get_all_expenses()

    return jsonify(expenses), 200

if __name__ == "__main__":
    app.run(debug=True)