# step_tracker.py
while True:
    total_steps = 0
    num_days = int(input("How many days do you want to track? "))

    for day in range(1, num_days + 1):
        steps = int(input(f"Enter the number of steps for day {day}: "))
        total_steps += steps

    average_steps = total_steps / num_days

    print(f"\nYou walked a total of {total_steps} steps over {num_days} days.")
    print(f"Your average steps per day: {average_steps:.0f}")

    if average_steps >= 10000:
        print("Awesome job!")
    else:
        print("Keep it up! Try to hit 10,000 a day.") 
    # Ask user if they want to track more
    continue_tracking = input("\nDo you want to track more days? (yes/no): ").strip().lower()
    if continue_tracking != "yes":
        print("Thanks for using the step tracker!")
        break
