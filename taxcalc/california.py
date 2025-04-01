def calculate_tax_and_net(salary):
    """
    Calculate California income tax and net income based on progressive tax brackets.
    Returns a tuple: (tax, net_income)
    """
    tax = 0
    brackets = [
        (9324, 0.01),
        (22107, 0.02),
        (34892, 0.04),
        (48435, 0.06),
        (61214, 0.08),
        (312686, 0.093),
        (375221, 0.103),
        (625369, 0.113),
        (float("inf"), 0.123)
    ]
    previous_limit = 0
    if salary <= 0:
        return 0.0, 0.0

    for limit, rate in brackets:
        if salary > limit:
            taxable_income = limit - previous_limit
        else:
            taxable_income = salary - previous_limit
        if taxable_income > 0:
            tax += taxable_income * rate
        if salary <= limit:
            break
        previous_limit = limit
    tax = round(tax, 2)
    net_income = round(salary - tax, 2)
    return tax, net_income
