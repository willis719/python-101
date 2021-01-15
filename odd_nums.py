def only_odds(num_list):
    return [num for num in num_list if num % 2 != 0]

print(only_odds([20, 35, 68, 21, 54, 58, 17]))