# import random

# def get_numbers_ticket(min, max, quantity):
#     random_number = set()
#     if min >= 1 and max <= 1000 and min <= quantity <= max:
#         for k in range(quantity):
#             random_number.add(random.randint(min, max))
#         print(random_number)
#     else:
#         print(random_number)

# get_numbers_ticket(1, 1000, 10)

import random

def get_numbers_ticket(min, max, quantity):
    random_number = set()
    if min >= 1 and max <= 1000:
        for k in range(quantity):
            random_number.add(random.randint(min, max))
        sorted_number = sorted(random_number)
        sorted_set = sorted(sorted_number)
        return sorted_set
    else:
        return random_number

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)