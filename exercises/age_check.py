# age_check.py
#expanded version: voting and age group
age = int(input("How old are you? "))
if age < 13:
    print("You're a child.")
elif age < 20:
    print("You're a teenager.")
elif age < 65:
    print("You're an adult.")
else:
    print("You're a senior.")

if age < 18:
    print("You're not old enough to vote.")
else:
    print("You're old enough to vote.")
