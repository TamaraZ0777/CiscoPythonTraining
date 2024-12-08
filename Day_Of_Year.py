def is_year_leap(year):
    #
    # Your code from the previous LAB.
    #
    if year < 1582:
        return None
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True    
    else:
        return False
        
def days_in_month(year, month):
    #
    # Your code from the previous lab.
    #
    if year < 1582 or month < 1 or month > 12:
        return None
    month_length = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    res = month_length[month - 1]
    if month == 2 and is_year_leap(year):
        res = 29
    return res

def day_of_year(year, month, day):
    #
    # Write your new code here.
    #
    days = 0

    for m in range(1, month):
        md = days_in_month(year, m)
        if md == None:
            return None
        days += md
    md = days_in_month(year, month)
    if day >= 1 and day <= md:
        return days + day
    else:
        return None


print(day_of_year(2000, 12, 31))
print(day_of_year(2024, 1, 25))
print(day_of_year(2024, 2, 12))

