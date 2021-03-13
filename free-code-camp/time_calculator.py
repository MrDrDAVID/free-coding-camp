def add_time(start, duration, day=None) :
    '''
    Function that takes in a time and any amount of hours/minutes
    to add to it, and returns the calculated time
    '''
    # Return value
    result = ''

    # All the times separated by hour, min and period
    time_hr = start.split(':')[0]
    time_min = start.split(':')[1].split()[0]
    time_ampm = start.split()[1]
    add_time_hr = duration.split(':')[0]
    add_time_min = duration.split(':')[1]

    # Constants for days of the week
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # Values to calculate
    total_min = 0
    total_hr = 0
    total_days = 0
    period = ''
    result_hr = ''
    result_min = ''

    total_min = int(time_min) + int(add_time_min)

    if total_min > 59 :
        total_min -= 60
        total_hr = int(time_hr) + int(add_time_hr) + 1
    else :
        total_hr = int(time_hr) + int(add_time_hr)
    
    if time_ampm == 'PM' :
        total_hr += 12

    total_days = total_hr//24

    if total_hr >= 12 and total_hr < 24 :
        period = 'PM'
        if total_hr > 12 :
            total_hr -= 12
    else :
        total_hr %= 24
        period = 'AM'
        if total_hr == 0 :
            total_hr = 12
        else :
            if total_hr > 12 :
                total_hr -= 12
                period = 'PM'

    result_hr = str(total_hr)
    if total_min < 10 :
        result_min = str(total_min).rjust(2, '0')
    else :
        result_min = str(total_min)

    if day == None :
        if total_days == 0 :
            result = result_hr + ':' + result_min + ' ' + period
        elif total_days == 1 :
            result = result_hr + ':' + result_min + ' ' + period + ' (next day)'
        else :
            result = result = result_hr + ':' + result_min + ' ' + period + ' (' + str(total_days) + ' days later)'
    else :
        calculated_day = (days.index(day.title()) + 1) + total_days
        calculated_day %= 7
        day = days[calculated_day - 1]

        if total_days == 0 :
            result = result_hr + ':' + result_min + ' ' + period + ', ' + day
        elif total_days == 1 :
            result = result_hr + ':' + result_min + ' ' + period + ', ' + day + ' (next day)'
        else :
            result = result = result_hr + ':' + result_min + ' ' + period + ', ' + day + ' (' + str(total_days) + ' days later)'

    return result


print(add_time("6:30 PM", "205:32"))
print(add_time("8:16 PM", "466:02"))
print(add_time("2:59 AM", "24:00"))