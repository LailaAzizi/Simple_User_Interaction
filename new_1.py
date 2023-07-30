game_list = [0, 1, 2]

def display_game(game_list):
    print("Here is the current list:")
    print(game_list)

def position_choice():
    acceptable_choice = ['0', '1', '2']
    while True:
        choice = input("Pick a position to replace (0, 1, 2): ")
        if choice in acceptable_choice:
            return choice
        else:
            try:
                int(choice)
                print("Sorry, but you did not choose a valid position (0, 1, 2)")
            except ValueError:
                print("Sorry, that is not a valid input. Please enter a digit (0, 1, 2)")

def replacement_choice(game_list, position):
    position = int(position)
    while True:
        user_placement = input(f"Type a string to place at position {position}: ")
        if user_placement.strip():  # Check if the input is not empty after stripping leading/trailing whitespace
            game_list[position] = user_placement
            print(f"The new list is {game_list}")
            return game_list
        else:
            print("Sorry, the input should not be empty. Try again.")

def gameon_choice():
    while True:
        choice = input("Would you like to keep playing? (Y or N): ").upper()

        if choice not in ['Y', 'N']:
            print("Sorry, I didn't understand. Please choose Y or N.")
        else:
            return choice == "Y"

game_on = True

while game_on:
    #print("Clear Screen and show the updated game list")
    #clear_output()
    display_game(game_list)

    # Have player choose position
    position = position_choice()

    # Rewrite that position and update game_list
    game_list = replacement_choice(game_list, position)

    # Ask if you want to keep playing
    game_on = gameon_choice()
