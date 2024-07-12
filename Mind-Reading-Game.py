def mind_reading_game():
    print("Welcome to the Mind Reading Game!")
    print("I'll guide you through each step. Press Enter after completing each step.")

    input("\nStep 1: Choose your age (but don't tell me). Press Enter when ready.")

    input("Step 2: Double your age. Press Enter when ready.")

    while True:
        try:
            added_number = int(input("Step 3: Add a number between 1 and 9. Enter that number here: "))
            if 1 <= added_number <= 9:
                break
            else:
                print("Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    input("Step 4: Divide the result by 2. Press Enter when ready.")

    input("Step 5: Subtract your original age. Press Enter when ready.")

    # Calculate the result
    result = added_number / 2

    print(f"\nBased on the steps you followed, your final result should be: {result}")
 

    print("\nWas I correct? (yes/no)")
    answer = input().lower()

    if answer == 'yes':
        print("Great! The mind reading trick worked!")
    else:
        print("Oops! Something went wrong. Let's try again!")

# Run the game
mind_reading_game()
