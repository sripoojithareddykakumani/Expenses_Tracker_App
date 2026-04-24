from flask import Flask, render_template, request, redirect, send_file
from database import get_connection, create_table, get_cursor
from datetime import datetime, timedelta
import csv, io, webbrowser, threading, os

app = Flask(__name__)
create_table()


@app.route("/")
def index():
    category = request.args.get("category")
    search = request.args.get("search")
    start = request.args.get("start")
    end = request.args.get("end")

    conn = get_connection()
    cursor = get_cursor(conn)

    # BASE QUERY
    query = "SELECT * FROM expenses WHERE 1=1"
    params = []

    # Use correct placeholder
    placeholder = "%s" if os.environ.get("DATABASE_URL") else "?"

    if category:
        query += f" AND category={placeholder}"
        params.append(category)

    if search:
        query += f" AND note LIKE {placeholder}"
        params.append(f"%{search}%")

    if start:
        query += f" AND date>={placeholder}"
        params.append(start)

    if end:
        query += f" AND date<={placeholder}"
        params.append(end)

    cursor.execute(query, params)
    expenses = cursor.fetchall()

    # TOTAL
    total = sum(e["amount"] for e in expenses)

    today = datetime.now().date()

    daily = 0
    weekly = 0
    last_week = 0
    monthly = 0

    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)

    last_week_start = start_of_week - timedelta(days=7)
    last_week_end = start_of_week - timedelta(days=1)

    current_month = today.strftime("%Y-%m")

    monthly_data = {str(i).zfill(2): 0 for i in range(1, 13)}
    category_totals = {}

    for e in expenses:
        if not e["date"]:
            continue

        dt = datetime.strptime(str(e["date"]), "%Y-%m-%d").date()
        amt = e["amount"]

        if dt == today:
            daily += amt

        if start_of_week <= dt <= end_of_week:
            weekly += amt

        if last_week_start <= dt <= last_week_end:
            last_week += amt

        if str(e["date"]).startswith(current_month):
            monthly += amt

        month = str(dt.month).zfill(2)
        monthly_data[month] += amt

        cat = e["category"]
        category_totals[cat] = category_totals.get(cat, 0) + amt

    category_totals = dict(
        sorted(category_totals.items(), key=lambda x: x[1], reverse=True)
    )

    cursor.execute("SELECT amount FROM budget WHERE id=1")
    budget_row = cursor.fetchone()
    budget = budget_row["amount"] if budget_row else 0

    percent = (total / budget * 100) if budget else 0

    conn.close()

    return render_template(
        "index.html",
        expenses=expenses,
        total=total,
        budget=budget,
        percent=percent,
        daily=daily,
        weekly=weekly,
        monthly=monthly,
        category_totals=category_totals,
        monthly_data=monthly_data,
        last_week=last_week
    )


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        conn = get_connection()
        cursor = get_cursor(conn)

        placeholder = "%s" if os.environ.get("DATABASE_URL") else "?"

        cursor.execute(
            f"INSERT INTO expenses (amount, category, date, note) VALUES ({placeholder}, {placeholder}, {placeholder}, {placeholder})",
            (
                request.form["amount"],
                request.form["category"],
                request.form["date"],
                request.form["note"]
            )
        )

        conn.commit()
        conn.close()
        return redirect("/")

    return render_template("add.html", current_date=datetime.now().strftime("%Y-%m-%d"))


@app.route("/delete/<int:id>")
def delete(id):
    conn = get_connection()
    cursor = get_cursor(conn)

    placeholder = "%s" if os.environ.get("DATABASE_URL") else "?"

    cursor.execute(f"DELETE FROM expenses WHERE id={placeholder}", (id,))
    conn.commit()
    conn.close()
    return redirect("/")


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    conn = get_connection()
    cursor = get_cursor(conn)

    placeholder = "%s" if os.environ.get("DATABASE_URL") else "?"

    if request.method == "POST":
        cursor.execute(
            f"""
            UPDATE expenses
            SET amount={placeholder}, category={placeholder}, date={placeholder}, note={placeholder}
            WHERE id={placeholder}
            """,
            (
                request.form["amount"],
                request.form["category"],
                request.form["date"],
                request.form["note"],
                id
            )
        )

        conn.commit()
        conn.close()
        return redirect("/")

    cursor.execute(f"SELECT * FROM expenses WHERE id={placeholder}", (id,))
    expense = cursor.fetchone()
    conn.close()

    return render_template("edit.html", expense=expense)


@app.route("/budget", methods=["POST"])
def set_budget():
    amount = request.form["budget"]

    conn = get_connection()
    cursor = get_cursor(conn)

    cursor.execute("DELETE FROM budget")
    cursor.execute("INSERT INTO budget (id, amount) VALUES (1, %s)" if os.environ.get("DATABASE_URL") else
                   "INSERT INTO budget (id, amount) VALUES (1, ?)", (amount,))

    conn.commit()
    conn.close()
    return redirect("/")


@app.route("/export")
def export():
    conn = get_connection()
    cursor = get_cursor(conn)

    cursor.execute("SELECT * FROM expenses")
    data = cursor.fetchall()

    conn.close()

    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["ID", "Amount", "Category", "Date", "Note"])

    for row in data:
        writer.writerow([row["id"], row["amount"], row["category"], row["date"], row["note"]])

    output.seek(0)

    return send_file(io.BytesIO(output.read().encode()),
                     mimetype="text/csv",
                     as_attachment=True,
                     download_name="expenses.csv")


def open_browser():
    webbrowser.open("http://127.0.0.1:5000")


if __name__ == "__main__":
    if not os.environ.get("WERKZEUG_RUN_MAIN"):
        threading.Timer(1, open_browser).start()
    app.run(debug=True)
