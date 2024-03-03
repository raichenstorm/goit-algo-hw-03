import datetime 

def get_days_from_today(date: str) -> int:
    user_input = input("Enter your date in 'YYYY-MM-DD' format: ")
    date = datetime.datetime.strptime(user_input, '%Y-%m-%d')
    print(date, type)
    # current_date = datetime.datetime.now()
    # delta_days = current_date - date