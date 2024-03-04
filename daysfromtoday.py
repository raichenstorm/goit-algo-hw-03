import datetime 

def get_days_from_today(date: str) -> int:
    try:
        user_date = datetime.datetime.strptime(date, '%Y-%m-%d')
        current_date = datetime.datetime.now()
        delta_days = (current_date - user_date).days
        print(delta_days)
    except ValueError:
        print("Your input is not in 'YYYY-MM-DD' format ")

get_days_from_today("2021-04-12")