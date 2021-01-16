from random import randrange

hotel = {
  '1': {
    '101': ['George Jefferson', 'Wheezy Jefferson'],
  },
  '2': {
    '237': ['Jack Torrance', 'Wendy Torrance'],
  },
  '3': {
    '333': ['Neo', 'Trinity', 'Morpheus']
  }
}



def check_in():
    #hotel[randrange(1, 4)] = {randrange(200, 300): [names]}
    hotel[floor_num] = {room_num: [names]}
    print(hotel)

def check_out():
    check_out_name = input("What is your name? ")
    del hotel[check_out_name]

status = input("Hello, would you like to check in or check out? ")
if status == "check in":
    total_guest = int(input("How many guest will there be? "))
    names = input("What are the names of the guest? ")
    floor_num = input("What floor would you like (1 - 3)? ")
    if floor_num == 1:
        room_num = randrange(100, 150)
    elif floor_num == 2:
        room_num = randrange(200, 250)
    elif floor_num == 3:
        room_num = randrange(300, 350)
    check_in() 
else:
    check_out()



    









