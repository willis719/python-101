counter = 0
while True:
    try:
        size = int(input("How big is the square? "))
        star = "*" * size
        while counter < size:
            print(star)
            counter += 1
        break
    except ValueError:
        print("Please type a number")
