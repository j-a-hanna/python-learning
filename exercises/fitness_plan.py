#fitness_plan.py

age = int(input("How old are you? "))
goal = input("What is your goal? (lose weight/build muscle): ").lower()
preferred_environment = input("Do you prefer indoor or outdoor workouts?: ").lower()
if goal not in ["lose weight", "build muscle"]:
    print("That's not a valid goal. Please choose 'lose weight' or 'build muscle'.")
elif preferred_environment not in ["indoor", "outdoor"]:
    print("Please enter 'indoor' or 'outdoor' for the environment.")
elif age < 18:
    print("You're too young for a formal plan — enjoy fun outdoor play and eat healthy!")
elif age > 65:
    print("Consider low-impact exercise like yoga or walking. Stay active and safe!")
elif age < 18:
    print("You're too young for a formal plan — enjoy fun outdoor play and eat healthy!")
elif age > 65:
    print("Consider low-impact exercise like yoga or walking. Stay active and safe!")

elif age < 30 and goal == "build muscle" and preferred_environment == "indoor":
    print("Try weightlifting at the gym 4 times a week.")
elif age >= 30 and goal == "build muscle" and preferred_environment == "indoor":
    print("Try low-impact resistance training with machines or light weights.")
elif goal == "lose weight" and preferred_environment == "outdoor":
    print("Outdoor running and a healthy diet will help you lose weight.")
elif goal == "lose weight" and preferred_environment == "indoor":
    print("Try HIIT classes or treadmill workouts indoors.")
else:
    print("Check with a fitness coach for personalized advice.")
