def get_user_password():
    return "gisele123"
def login():
    max_trials = 3
    remaining_trials = max_trials
    stored_password = get_user_password()
    while remaining_trials > 0:
        user_input = input("Enter your password: ")
        if user_input == stored_password:
            print("Login successful!")
            return True
        else:
            remaining_trials -= 1
            if remaining_trials > 0:
                print(f"Wrong password! {remaining_trials} trial(s) left.")
            else:
                print("Get out!")
    return False
if __name__ == "__main__":
    if login():
        print("Welcome to the system!")
    else:
        print("Login failed. Exiting...")
