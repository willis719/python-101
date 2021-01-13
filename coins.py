coin = 0
print(f"You have {coin} coins")
answer = ("Do you want another coin? ")

while answer == "yes":
    coin += 1
    print(f"You have {coin} coins.")
    if answer == "no":
        print("Bye")