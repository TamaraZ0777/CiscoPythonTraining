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
        
days = 0

def days_in_month(year, month):
    months_length = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_year_leap(year):
        months_length[1] = 29
    days = months_length[month-1]
    return days

test_years = [1900, 2000, 2016, 1987, 2025, 2024]
test_months = [2, 2, 1, 11, 2, 10]
test_results = [28, 29, 31, 30, 28, 31]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")

    