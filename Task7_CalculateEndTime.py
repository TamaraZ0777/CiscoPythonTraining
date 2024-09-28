hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# if dura < 60:
#     new_mins = mins + dura
#     new_hours = hour
#     if new_mins >= 60:
#         new_hours += 1
#         new_mins -= 60

#     if new_hours >= 24:
#         new_hours -= 24

# else:
#     add_hours = dura // 60
#     new_hours = hour
#     new_hours += add_hours
#     add_mins = dura % 60
#     new_mins = mins
#     new_mins += add_mins
#     if new_mins >= 60:
#         new_hours += 1
#         new_mins -= 60

#     if new_hours >= 24:
#         new_hours %= 24 

#Trying to create a shorter solution:

total_mins = mins + dura
additional_hours = total_mins // 60
new_hours = (hour + additional_hours) % 24
new_mins = total_mins % 60

print("End Time is", new_hours, ":", new_mins)

