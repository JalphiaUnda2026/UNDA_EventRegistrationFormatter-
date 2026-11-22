
# VERSION 2: String Formatting

print("Student Event Registration Summary")

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
section = input("Enter section: ")
event_name = input("Enter event name: ")

year = input("Enter event year: ")
month = input("Enter event month: ")
day = input("Enter event day: ")

first_name = first_name.strip().title()
last_name = last_name.strip().title()
section = section.strip().upper()
event_name = event_name.strip().title()

full_name = first_name + " " + last_name
name_code = full_name.upper()

print("\nStudent Event Registration Summary")
print("Name:", full_name)
print("Name Code:", name_code)
print("Section:", section)
print("Event:", event_name)
print("Event Date:", month, day + ",", year)

print("\nLanguage Used: Python")
print("String Feature Used: strip(), title(), upper()")
print("Registration record created successfully.")
