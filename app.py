from flask import Flask, render_template, request
from taxcalc.california import calculate_tax_and_net

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    tax_due = None
    net_income = None
    salary = None
    error_message = None

    if request.method == "POST":
        try:
            salary_str = request.form.get("salary", "").strip()
            if not salary_str:
                raise ValueError("Salary input is empty.")
            salary = float(salary_str)
            if salary < 0:
                raise ValueError("Enter a valid (non-negative) number.")
            tax_due, net_income = calculate_tax_and_net(salary)
        except Exception as e:
            error_message = "Error calculating tax: " + str(e)
    
    return render_template("index.html", tax_due=tax_due, net_income=net_income, salary=salary, error_message=error_message)

if __name__ == "__main__":
    app.run(debug=True)
