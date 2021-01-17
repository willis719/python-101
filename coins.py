coin = 0
print(f"You have {coin} coins")
answer = input("Do you want another coin? ")
    

while answer == "yes":
    coin += 1
    print(f"You have {coin} coins.")
    answer = input("Do you wan another coin? ")
if answer == "no":
    print("Bye")


