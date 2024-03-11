import random

def get_numbers_ticket(min, max, quantity):
    random_number = set()
    if min >= 1 and max <= 1000:
        while len(random_number) < quantity:
            random_number.add(random.randint(min, max))
        return sorted(random_number)
    else:
        return random_number

lottery_numbers = get_numbers_ticket(10, 15, -5)
print("Ваші лотерейні числа:", lottery_numbers)