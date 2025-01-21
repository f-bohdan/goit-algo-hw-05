import datetime 

def get_days_from_today(date):
    # to get todays date:
    today = datetime.datetime.today().date()
    # for catching Errors
    try:
        # get difference btwn today and entered date
        diff = (today-datetime.datetime.strptime(date, "%Y-%m-%d").date()).days
    except ValueError:
        print("Enter correct date in format YYYY-MM-DD")
        return 0
    return int(diff)

print(get_days_from_today("2024-10-09"))