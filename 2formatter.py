import datetime

title = input("Enter event title: ").strip()
year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))

date_obj = datetime.date(year, month, day)

print("\nFormatted Output:")
print("Event:", title.upper())
print("Date:", date_obj.strftime("%B") + " " + str(date_obj.day) + ", " + str(date_obj.year))
print("Year:", date_obj.year)
print("Month:", date_obj.strftime("%B"))
print("Day:", date_obj.day)
print("Weekday:", date_obj.strftime("%A"))
