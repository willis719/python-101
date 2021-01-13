total = int(input("What was the total bill amount? $"))
service = input("Was the service good, fair or bad? ")
split = int(input("Split how many ways? "))




if service == "good":
    tip = .20 * total
    total_amount = total + tip
    per_person = total_amount / split
    print(f"Tip amount: ${tip}")
    print(f"Total amount: ${total_amount}")
    print(f"Amount per person: ${per_person}")
elif service == "fair":
    tip = .15 * total
    total_amount = total + tip
    per_person = total_amount / split
    print(f"Tip amount: ${tip}")
    print(f"Total amount: ${total_amount}")
    print(f"Amount per person: ${per_person}")
elif service == "bad":
    tip = .10 * total
    total_amount = total + tip
    per_person = total_amount / split
    print(f"Tip amount: ${tip}")
    print(f"Total amount: ${total_amount}")
    print(f"Amount per person: ${per_person}")
else:
    print("Please read the instructions")