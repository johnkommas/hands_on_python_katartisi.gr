import random

num_people_in_room = 120  # Change This Number min: 2 max: 83


# Simulate a room with a certain number of people
def simulate(num_people):
    birthdays = []
    print("Here's what our room looks like:\n")
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]
    # Assign a random birthday to each person
    for i in range(0, num_people):
        # Choose a random month
        month_choice = random.choice(months)
        # Choose a random day based on month
        if month_choice == "February":
            day = random.randint(1, 29)
        elif month_choice in ("April", "June", "September", "November"):
            day = random.randint(1, 30)
        else:
            day = random.randint(1, 31)
        birthday = f'{month_choice} {day}'
        # Store the birthday
        birthdays.append(birthday)
        print(f"Person {i + 1}'s birthday: {birthday}")
    calculate_probability(num_people)
    match = False
    # Check for matching birthdays
    for i in range(len(birthdays)):
        if find_duplicates(birthdays, birthdays[i], i):
            match = True
            break
    if not match:
        print("\n\nIn our simulation, no two people have the same birthday")


# Calculate the probability of there being 2 people with the same birthday
def calculate_probability(num_people):
    # Check there is at least 2 people in the room
    if num_people < 2:
        print("\n\nNot enough people in the room!")
        return
    else:
        # Calculate the probability
        numerator = 365
        countdown = 364
        for i in range(2, num_people + 1):
            numerator = numerator * countdown
            countdown -= 1
        denominator = 365 ** num_people
        probability = 1 - numerator / float(denominator)
        # Change probability to percentage
        rounded = round(probability * 100, 2)
        print(
            f"\n\nThe probability that two people in a room of {num_people} people have the same birthday is nearly {rounded}%")


# Find the same birthday within our list of birthdays
def find_duplicates(birthdays_list, birthday, index):
    people = []
    for i in range(len(birthdays_list)):
        if birthdays_list[i] == birthday and i != index:
            people.append(i + 1)
    if people:
        people.append(index + 1)
        print("\n\nIn our simulation, the following people have the same birthdays: ")
        for person in people:
            print(f"Person {person}")
        return True
    else:
        return False


simulate(num_people_in_room)
