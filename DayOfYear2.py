def is_year_leap(year):

    if year < 1582:
        print("The year is before Gregorian calendar went into effect")
    else:
        if year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False
        elif year % 4 == 0:
            return True
        else:
             return False
        
def days_in_month(year, month):
    months_length = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_year_leap(year):
        months_length[1] = 29
    days = months_length[month-1]
    return days

def day_of_year(year, month, day):
    sum = 0
    for i in range(1, month):
        sum += days_in_month(year, i)
    sum +=day
    return sum
    #print("This is the day ", sum)

print(day_of_year(2001, 12, 31))

