from datetime import datetime, timedelta  # Імпорт класів datetime та timedelta для роботи з датами і часом

users = [  # Список користувачів з їхніми датами народження
    {"name": "John Doe", "birthday": "1985.03.12"},
    {"name": "Jane Smith", "birthday": "2020.03.10"}
]

def get_prepared_users(users):
    prepared_users = []  # Список підготовлених користувачів
    for user in users:  # Ітерація по кожному користувачеві зі списку
        try:
            birthday = datetime.strptime(user['birthday'], '%Y.%m.%d').date()  # Парсимо дату народження
            prepared_users.append({"name": user['name'], 'birthday': birthday})  # Додаємо користувача з підготовленою датою народження
        except ValueError:
            print(f'Некоректна дата народження для користувача {user["name"]}')  # Виводимо повідомлення про помилку
    return prepared_users

def find_next_weekday(d, weekday: int):  # Функція для знаходження наступного заданого дня тижня після заданої дати
    days_ahead = weekday - d.weekday()  # Різниця між заданим днем тижня та днем тижня заданої дати
    if days_ahead <= 0:  # Якщо день народження вже минув
        days_ahead += 7  # Додаємо 7 днів, щоб отримати наступний тиждень
    return d + timedelta(days=days_ahead)  # Повертаємо нову дату

def get_upcoming_birthdays(users):
    prepared_users = get_prepared_users(users)
    days = 7  # Кількість днів для перевірки на наближені дні народження
    today = datetime.today().date()  # Поточна дата

    upcoming_birthdays = []  # Список майбутніх днів народження
    for user in prepared_users:  # Ітерація по підготовленим користувачам
        birthday_this_year = user["birthday"].replace(year=today.year)  # Заміна року на поточний для дня народження цього року

        if birthday_this_year < today:  # Якщо дата народження вже пройшла цього року
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)  # Переносимо наступний рік

        if 0 <= (birthday_this_year - today).days <= days:  # Якщо день народження в межах вказаного періоду
            if birthday_this_year.weekday() >= 5:  # Якщо день народження випадає на суботу або неділю
                birthday_this_year = find_next_weekday(birthday_this_year, 0)  # Знаходимо наступний понеділок

            congratulation_date_str = birthday_this_year.strftime('%Y.%m.%d')  # Форматуємо дату у рядок
            upcoming_birthdays.append({  # Додаємо дані про майбутній день народження
                "name": user["name"],
                "congratulation_date": congratulation_date_str
            })
    return upcoming_birthdays

print(get_upcoming_birthdays(users))