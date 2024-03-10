import datetime 

def get_days_from_today(date: str) -> int:
    try:
        user_date = datetime.datetime.strptime(date, '%Y-%m-%d')
        current_date = datetime.datetime.now()
        delta_days = (current_date - user_date).days
    except ValueError:
        print("Your input is not in 'YYYY-MM-DD' format ")
    return delta_days

print(get_days_from_today("2024-03-11"))