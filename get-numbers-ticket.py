import random

def get_numbers_ticket(min, max, quantity):
    random_number = set()
    if min >= 1 and max <= 1000 and min <= quantity <= max:
        for k in range(quantity):
            random_number.add(random.randint(min, max))
        print(random_number)
    else:
        print(random_number)

    

get_numbers_ticket(1, 1000, 5)