def greet_user():
    name = input("What is your name?: ")

    time = int(input("What is the time? (0-23): "))

    if 0 <= time <= 12:
        print(f"Good morning, {name}!")
    elif 13 <= time <= 17:
        print(f"Good afternoon, {name}!")
    elif 18 <= time <= 23:
        print(f"Good evening, {name}!")
    else:
        print("Invalid time entered. Please enter a time between 0 and 23.")

greet_user()
