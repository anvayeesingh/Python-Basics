
medical_cause = input("Did you have a medica cause? (Y/N)").strip().upper()

if medical_cause == "Y":
    print("You allowed to take the exam")

else:
    attendance = int(input("Enter attendace of student"))

    if attendance >= 75:
     print("Allowed ")
    else:
     print("Not allowed")
