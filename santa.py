def santa():
    wish = input("What do you want for Christmas? ")
    behavior = input("Have you been good or bad this year? ")
    if behavior == "good":
        print(f"You will recieve a {wish}")
    elif behavior == "bad":
        print("You will get a lump of coal")
    else: 
        print("Invalid response.")

santa()