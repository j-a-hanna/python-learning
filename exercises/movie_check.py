# movie_check.py

age = int(input("How old are you? "))
has_ticket = input("Do you have a ticket? (yes/no): ").lower()

if age >= 13 and has_ticket == "yes":
    print("You're allowed to watch a movie. 🎬")
else:
    print("Sorry, you can't enter.")
