password = "12345"
tries = 4

while tries > 0:
    user_input = input("Enter password: ")
    if user_input == password:
        print("You are now Logged in to the system.")
        break
    else:
        tries -= 1  # tries=tries-1
        if tries == 0:
            print("You have been kicked off of the system.")
        else:
            print("Incorrect password. You have", tries, "tries")
