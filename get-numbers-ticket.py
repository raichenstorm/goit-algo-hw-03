import random

def get_numbers_ticket(min, max, quantity):
    random_number = set()
    if min < 1 or max > 1000 or quantity < 1 or quantity > (max - min + 1):
        print("Неправильні параметри. Перевірте, щоб min був не менше 1, max не більше 1000, а кількість чисел в діапазоні від min до max.")
        return sorted(random_number)
    else:
        while len(random_number) < quantity:
            random_number.add(random.randint(min, max))
        return sorted(random_number)

lottery_numbers = get_numbers_ticket(1, 5, 6)
print(f"Ваші лотерейні числа: {lottery_numbers}")

# elif min >= 1 and max <= 1000: