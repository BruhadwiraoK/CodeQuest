import time
import hashlib

# Simulate a database for user accounts
users = {}

def hash_password(password):
    """Securely hash passwords."""
    return hashlib.sha256(password.encode()).hexdigest()

def register():
    """Register a new user."""
    print("\n=== Register ===")
    username = input("Enter username: ")
    if username in users:
        print("Username already exists. Try logging in.")
        return False
    password = input("Enter password: ")
    users[username] = {"password": hash_password(password), "points": 0}
    print(f"User '{username}' registered successfully!")
    return True

def login():
    """Login an existing user."""
    print("\n=== Login ===")
    username = input("Enter username: ")
    if username not in users:
        print("Username not found. Please register.")
        return None
    password = input("Enter password: ")
    if users[username]["password"] == hash_password(password):
        print(f"Welcome back, {username}!")
        return username
    print("Invalid password.")
    return None

def game_menu(username):
    """Display the game menu."""
    while True:
        print("\n=== Game Menu ===")
        print("1. Start Game")
        print("2. View Points")
        print("3. Logout")
        choice = input("Enter your choice: ")
        if choice == "1":
            start_game(username)
        elif choice == "2":
            print(f"{username}, you have {users[username]['points']} points.")
        elif choice == "3":
            print(f"Goodbye, {username}!")
            break
        else:
            print("Invalid choice. Please try again.")

def start_game(username):
    """Start the game."""
    print("\n=== Code Quest ===")
    levels = [
        {"question": "What is 5 + 3?", "answer": "8"},
        {"question": "What is the output of print(2 ** 3)?", "answer": "8"},
        {"question": "Solve: 12 / 4 + 2 * 3", "answer": "9.0"}
    ]
    for i, level in enumerate(levels):
        print(f"\nLevel {i + 1}: {level['question']}")
        start_time = time.time()
        answer = input("Your answer: ")
        elapsed_time = time.time() - start_time
        if answer == level["answer"]:
            users[username]["points"] += 10
            print("Correct! You earned 10 points.")
        else:
            users[username]["points"] -= 5
            print("Wrong answer! You lost 5 points.")
        if elapsed_time > 30:  # Penalize for idle behavior
            users[username]["points"] -= 10
            print("Too slow! You lost 10 points for idling.")

def main():
    """Main function to run the game."""
    while True:
        print("\n=== Welcome to Code Quest ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            register()
        elif choice == "2":
            user = login()
            if user:
                game_menu(user)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
