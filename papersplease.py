import random

random_names = {
    1: "Liam",
    2: "Olivia",
    3: "Noah",
    4: "Emma",
    5: "Jackson",
    6: "Ava",
    7: "Aiden",
    8: "Isabella",
    9: "Lucas",
    10: "Sophia",
    11: "Ethan",
    12: "Mia",
    13: "Mason",
    14: "Amelia",
    15: "Caden",
    16: "Harper",
    17: "Oliver",
    18: "Evelyn",
    19: "Elijah",
    20: "Abigail",
    21: "Grayson",
    22: "Emily",
    23: "Michael",
    24: "Elizabeth",
    25: "Benjamin",
    26: "Sofia",
    27: "Carter",
    28: "Scarlett",
    29: "Alexander",
    30: "Victoria",
    31: "James",
    32: "Aria",
    33: "William",
    34: "Grace",
    35: "Luke",
    36: "Chloe",
    37: "Henry",
    38: "Lily",
    39: "Daniel",
    40: "Zoey",
    41: "Matthew",
    42: "Penelope",
    43: "Joseph",
    44: "Layla",
    45: "Samuel",
    46: "Riley",
    47: "David",
    48: "Nora",
    49: "John",
    50: "Eleanor"
}

def start_menu():
    print("=== Start Menu ===")
    print("[1] Start Game")
    print("[0] Exit")

def start_game():
    print("Starting a new game...")
    # Your game logic goes here.

def exit_game():
    print("Exiting the program...")
    # You can add any cleanup or saving tasks before exiting here if needed.
    exit()

def manual():
    print("=== Manual ===")
    print("Welcome to the game manual/tutorial.")
    print("This game is a rip-off of the Papers Please game, so heres how to play read lol and also there is no user-interface for the face-id I will just add the face-id button lol.")
    print("Press [0] to Exit manual.")

def conversation(current_person=None, accepted_persons=None, declined_persons=None):
    if accepted_persons is None:
        accepted_persons = []
    if declined_persons is None:
        declined_persons = []

    if current_person is None:
        random_index = random.randint(1, 50)
        current_person = random_names[random_index]

    while current_person in accepted_persons or current_person in declined_persons:
        random_index = random.randint(1, 50)
        current_person = random_names[random_index]

    print(f"You: Give papers please!")
    print(f"{current_person}: Hello, this is my papers.")
    return current_person

def action_menu():
    print("=== Action Menu ===")
    print("[1] Accept person")
    print("[2] Decline person")
    print("[3] Check ID")
    print("[4] Shoot person")
    print("[0] Exit without saving")

def check_id():
    success_chance = random.random()  # Generates a random float between 0 and 1
    return success_chance > 0.25

def main():
    accepted_persons = []
    declined_persons = []
    current_person = None
    shot_count = 0

    while True:
        start_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            start_game()
        elif choice == '2':
            load_game()
        elif choice == '0':
            exit_game()
        else:
            print("Invalid choice. Please select a valid option.")

        if choice == '1':
            while True:
                manual()
                manual_choice = input("Enter your choice: ")
                if manual_choice == '0':
                    break

            # After exiting the manual, display the conversation.
            current_person = conversation(current_person, accepted_persons, declined_persons)

            # Display the action menu after the conversation.
            while True:
                action_menu()
                action_choice = input("Enter your choice: ")

                if action_choice == '1':
                    print(f"{current_person}: Thank you, glory to ####")
                    accepted_persons.append(current_person)
                    current_person = conversation(None, accepted_persons, declined_persons)  # New person comes in
                elif action_choice == '2':
                    print(f"{current_person}: I'll remember this...")
                    declined_persons.append(current_person)
                    current_person = conversation(None, accepted_persons, declined_persons)  # New person comes in
                elif action_choice == '3':
                    if check_id():
                        print("ID check successful. You can let the person through.")
                        accepted_persons.append(current_person)
                        current_person = conversation(None, accepted_persons, declined_persons)  # New person comes in
                    else:
                        print("ID check failed.")
                        choice_after_failure = input("Do you want to let the person through? (yes/no): ")
                        if choice_after_failure.lower() == "yes":
                            print("You let the person through, but you were exploded!")
                            exit_game()
                        else:
                            print(f"{current_person}: I'm not leaving until you let me through!")
                            declined_persons.append(current_person)
                            current_person = conversation(None, accepted_persons, declined_persons)  # New person comes in
                elif action_choice == '4':
                    shot_count += 1
                    if shot_count == 5:
                        print("You have shot 5 people! The authorities are after you.")
                        exit_game()
                    else:
                        print(f"{current_person}: You won't get away with this!")
                        print("Shooting the person...")
                        declined_persons.append(current_person)
                        current_person = conversation(None, accepted_persons, declined_persons)  # New person comes in
                elif action_choice == '0':
                    print("Exiting the game without saving...")
                    exit_game()
                else:
                    print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

