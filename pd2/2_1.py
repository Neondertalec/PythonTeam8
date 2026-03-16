def compute_wage(hours, rate):
    if hours > 40:
        regular_pay = 40 * rate
        overtime_hours = hours - 40
        overtime_pay = overtime_hours * rate * 2.10
        total_pay = regular_pay + overtime_pay
    else:
        total_pay = hours * rate
    return total_pay

# Example usage:
hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

pay = compute_wage(hours, rate)
print("Pay:", pay)
