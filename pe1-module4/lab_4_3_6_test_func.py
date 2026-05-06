import lab_4_3_5_day_count as lab

year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))

result = lab.day_of_year(year, month, day)

if result is None:
    print("Invalid date")
else:
    print("Day of the year:", result)



