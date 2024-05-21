hour = eval(input("Enter the current hour (1-12): "))
meridian = input("Enter 'AM' or 'PM': ")
offset = eval(input("How many hours ahead? "))

new_hour = (hour + offset) % 12
if new_hour == 0:
    new_hour = 12

if (hour + offset) >= 12:
    if meridian == "AM":
        new_meridian = "PM"
    else:
        new_meridian = "AM"
else:
    new_meridian = meridian

print("New Hour: ", new_hour, new_meridian)
