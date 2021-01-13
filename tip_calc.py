total = int(input("What was the total bill amount? $"))
service = input("Was the service good, fair or bad? ")


if service == "good":
    tip = .20 * total
    total_amount = total + tip
    print(f"Tip amount: ${tip}")
    print(f"Total amount: ${total_amount}")
elif service == "fair":
    tip = .15 * total
    total_amount = total + tip
    print(f"Tip amount: ${tip}")
    print(f"Total amount: ${total_amount}")
elif service == "bad":
    tip = .10 * total
    total_amount = total + tip
    print(f"Tip amount: ${tip}")
    print(f"Total amount: ${total_amount}")
else:
    print("Please read the instructions")
    