import uuid

# Simulated database using a dictionary
user_db = {}

# Function to add a new user
def add_user(name, email):
    user_id = str(uuid.uuid4()) # generate a unique ID
    user_db[user_id] = {
        "name": name,
        "email": email
    }
    return user_id

# Function to retrieve user by UUID
def get_user(user_id):
    return user_db.get(user_id, "User not found")

# Add a few users
uid1 = add_user("Alice", "alice@example.com")
uid2 = add_user("Bob", "bob@example.com")

# Display the databae
print("User Database:")
for uid, data in user_db.items():
    print(f"{uid}: {data}")

#Retrieve a user
print("\nRetrieving a user by UUID:")
print(get_user(uid1))
