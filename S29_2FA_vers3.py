
# VERSION 3: Event Registration Formatter

from datetime import datetime

print("STUDENT EVENT REGISTRATION")
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
section = input("Enter section: ")
event_name = input("Enter event name: ")

year = int(input("Enter event year: "))
month = int(input("Enter event month (1-12): "))
day = int(input("Enter event day: "))
first_name = first_name.strip().title()
last_name = last_name.strip().title()
section = section.strip().upper()
event_name = event_name.strip().title()


full_name = first_name + " " + last_name
name_code = full_name.upper()

event_date = datetime(year, month, day)
formatted_date = f"{event_date:%B} {event_date.day}, {event_date.year}"

print("\nStudent Event Registration Summary")
print("-----------------------------------")
print("Name:", full_name)
print("Name Code:", name_code)
print("Section:", section)
print("Event:", event_name)
print("Event Date:", formatted_date)

print("\nLanguage Used: Python")
print("String Feature Used: strip(), title(), upper()")
print("Date/Time Feature Used: datetime")

print("\nRegistration record created successfully.")
