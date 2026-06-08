def due_amount(bill, paid):
    return bill - paid

bill_amount = float(input("Enter the bill amount: "))
paid_amount = float(input("Enter the amount paid: "))

due = due_amount(bill_amount, paid_amount)

print("Customer's due amount =", due)