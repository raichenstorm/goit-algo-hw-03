import datetime 

def get_days_from_today(date: str) -> int:
    try: 
        user_input = input("Enter your date in 'YYYY-MM-DD' format: ")
    except Exception:
        print("Your input is not in 'YYYY-MM-DD" )
    finally:
        date = datetime.datetime.strptime(user_input, '%Y-%m-%d')
        current_date = datetime.datetime.now()
        delta_days = (current_date - date).days
        print(delta_days)


get_days_from_today("2024-05-05")