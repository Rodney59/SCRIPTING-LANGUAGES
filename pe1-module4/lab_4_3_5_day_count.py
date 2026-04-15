import lab_4_3_4_leap_year
def days_in_month(year, month):
    # validate inputs
    if year < 1 or month < 1 or month > 12:
        return None

    # days in months (index 0 = January)
    days = [31, 28, 31, 30, 31, 30,
            31, 31, 30, 31, 30, 31]

    # handle February
    if month == 2 and lab_4_3_4_leap_year.is_year_leap(year):
        return 29

    return days[month - 1]
year = int(input("Enter year: "))
month = int(input("Enter month (1-12): "))

result = days_in_month(year, month)

# printing result
if result is None:
    print("Invalid input.")
else:
    print("Number of days:", result)