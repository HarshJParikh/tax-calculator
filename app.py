from flask import Flask, render_template, request
from taxcalc.california import calculate_tax_and_net

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    tax_due = None
    net_income = None
    salary = None
    if request.method == "POST":
        try:
            salary = float(request.form.get("salary"))
            tax_due, net_income = calculate_tax_and_net(salary)
        except Exception as e:
            tax_due = "Error calculating tax: " + str(e)
    return render_template("index.html", tax_due=tax_due, net_income=net_income, salary=salary)

if __name__ == "__main__":
    app.run(debug=True)
