import bcrypt
import getpass

# Function to hash the password
def hash_password(plain_password):
    # Generate a salt
    salt = bcrypt.gensalt()
    # Hash the password with the salt
    hashed_password = bcrypt.hashpw(plain_password.encode('utf-8'), salt)
    return hashed_password

# Function to verify the password
def check_password(stored_hash, plain_password):
    # Check if the provided password matches the stored hashed password
    return bcrypt.checkpw(plain_password.encode('utf-8'), stored_hash)

# Register (hash and store the password)
def register_user():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    
    # Hash the password
    hashed_password = hash_password(password)
    
    # Store the username and hashed password (For demo, we will use a dictionary)
    # In a real application, you would store this in a database.
    user_db[username] = hashed_password
    print(f"User '{username}' registered successfully!")

# Login (authenticate the user)
def login_user():
    username = input("Enter your username: ")
    
    # Check if the username exists
    if username not in user_db:
        print("Username not found.")
        return
    
    password = getpass.getpass("Enter your password: ")
    
    # Retrieve the stored hash from the "database"
    stored_hash = user_db[username]
    
    # Verify the password
    if check_password(stored_hash, password):
        print("Authentication successful!")
    else:
        print("Invalid password.")

# Demo application
if __name__ == "__main__":
    # This dictionary simulates a "database" of users
    user_db = {}

    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            register_user()
        elif choice == "2":
            login_user()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
