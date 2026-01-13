
lineup = [
    ("Code Play", "Indie", 30),
    ("The Pythonistas", "Rock", 45),
    ("Syntax Error", "Metal", 60)

]

while True:
    print("--Pyfest Lineup Stage Management--")
    print("1. View lineup and total duration")
    print("2. Add a new band")
    print("3. Move first band to the end (late start)")
    print("4. Remove a band by name")
    print("5. Move band to specific position")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        print(lineup)
        total_duration = sum(band[2] for band in lineup)
        print("Total duration:", total_duration)

    elif choice == "2":
        name = input("Enter band name: ")
        genre = input("Enter band genre: ")
        try:
            duration = int(input("Enter performance duration (minutes): "))
        except ValueError:
            print("Invalid duration. Please enter a number.")
        else:
            lineup.append((name, genre, duration))
            print(name + " added")

    elif choice == "3":
        if lineup:
            lineup.append(lineup.pop(0))
            print("First band moved to the end.")
        else:
            print("Lineup is empty.")

    elif choice == "4":
        name_to_remove = input("Enter the name of the band to remove: ")
        for band in lineup:
            if band[0].lower() == name_to_remove.lower():
                lineup.remove(band)
                print(f"{name_to_remove} removed.")
                break
        else:
            print(f"Band {name_to_remove} not found.")

    elif choice == "5":
        name_to_move = input("Enter the name of the band to move: ")
        try:
            new_position = int(input("Enter the new position (1-based index): ")) - 1
            for band in lineup:
                if band[0].lower() == name_to_move.lower():
                    lineup.remove(band)
                    lineup.insert(new_position, band)
                    print(f"{name_to_move} moved to position {new_position + 1}.")
                    break
            else:
                print(f"No band found with the name {name_to_move}.")
        except ValueError:
            print("Invalid position. Please enter a number.")

    elif choice == "6":
        print("Exiting Stage Manager. Have a great show!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 6.")


