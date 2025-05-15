#weekend_planner.py

day = input("What day is it today? ").lower()
is_raining = input("Is it raining? (yes/no): ").lower()

if (day == "saturday" or day == "sunday") and is_raining == "no":
    print("Great day for a hike! 🥾")
elif (day == "saturday" or day == "sunday") and is_raining == "yes":
    print("Stay in and watch movies. 🍿")
else:
    print("Back to work or school! 🏫")

if not is_raining == "yes":
    print("It's dry outside.")
