Instructions = """
Build a Time Calculator Project

Write a function named add_time that takes in two required parameters and one optional parameter:

a start time in the 12-hour clock format (ending in AM or PM)
a duration time that indicates the number of hours and minutes
(optional) a starting day of the week, case insensitive
The function should add the duration time to the start time and return the result.

If the result will be the next day, it should show (next day) after the time. 
If the result will be more than one day later, it should show (n days later) after the time, where "n" is the number of days later.

If the function is given the optional starting day of the week parameter, then the output should display the day of the week of the result. 
The day of the week in the output should appear after the time and before the number of days later.

Below are some examples of different cases the function should handle. Pay close attention to the spacing and punctuation of the results.

Example Code
add_time('3:00 PM', '3:10')
# Returns: 6:10 PM

add_time('11:30 AM', '2:32', 'Monday')
# Returns: 2:02 PM, Monday

add_time('11:43 AM', '00:20')
# Returns: 12:03 PM

add_time('10:10 PM', '3:30')
# Returns: 1:40 AM (next day)

add_time('11:43 PM', '24:20', 'tueSday')
# Returns: 12:03 AM, Thursday (2 days later)

add_time('6:30 PM', '205:12')
# Returns: 7:42 AM (9 days later)

Do not import any Python libraries. Assume that the start times are valid times. 
The minutes in the duration time will be a whole number less than 60, but the hour can be any whole number.
"""




def add_time(start, duration, day_of_week=None):
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    # Parse start time
    time_part, meridian = start.split()
    start_hour, start_minute = map(int, time_part.split(':'))
    
    # Convert start time to 24-hour format
    if meridian == "PM" and start_hour != 12:
        start_hour += 12
    elif meridian == "AM" and start_hour == 12:
        start_hour = 0
    
    # Parse duration time
    duration_hour, duration_minute = map(int, duration.split(':'))
    
    # Add duration to start time
    total_minutes = start_minute + duration_minute
    extra_hours = total_minutes // 60
    total_minutes %= 60
    
    total_hours = start_hour + duration_hour + extra_hours
    total_days = total_hours // 24
    total_hours %= 24
    
    # Convert back to 12-hour format
    new_meridian = "AM" if total_hours < 12 else "PM"
    new_hour = total_hours if 1 <= total_hours <= 12 else total_hours % 12 or 12
    
    # Determine new day of the week if provided
    if day_of_week:
        day_index = (days_of_week.index(day_of_week.capitalize()) + total_days) % 7
        new_day = f", {days_of_week[day_index]}"
    else:
        new_day = ""
    
    # Determine day suffix
    if total_days == 1:
        day_suffix = " (next day)"
    elif total_days > 1:
        day_suffix = f" ({total_days} days later)"
    else:
        day_suffix = ""
    
    return f"{new_hour}:{total_minutes:02d} {new_meridian}{new_day}{day_suffix}"



# Test Cases
print(add_time('3:30 PM', '2:12'))

print(add_time('11:55 AM', '3:12'))

