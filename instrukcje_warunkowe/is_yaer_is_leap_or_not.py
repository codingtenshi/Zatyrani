def get_leap_year(year):
    if year % 4 == 0 and year % 100 != 0:
        return "Leap year"
    else:
        return "Not leap year"



