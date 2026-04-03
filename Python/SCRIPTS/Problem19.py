# 1st january 1901 - 31st december 2000
# 1st january 1900 - Monday

Week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
Y365 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
Y366 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# weekday of 1st januare 1901
day_count = 1
w_index = 0
while day_count <= 365:
    day_count += 1
    w_index += 1

    if w_index % 7 == 0: w_index = 0


# daycount off all years 1901 - 2000
Years = []
for year in range(1901, 2001):
    if year % 4 == 0: Years.append(Y366)
    else: Years.append(Y365)

# count sundays per year 
sunday_count = 0
for year in Years:
    for month in year:
        count = 0
        while count < month:

            if w_index == 6 and count == 0:
                sunday_count += 1

            count += 1
            w_index += 1

            if w_index % 7 == 0:
                w_index = 0

print(sunday_count)