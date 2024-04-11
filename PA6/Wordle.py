import random

class Wordle:
    """ Wordle game class adds all the components to create the game Wordle """
    def __init__(self, attempts, word_length):
        self.max_attempts = attempts # The attempts you started with
        self.attempts = attempts # How many attempts you have to solve the game
        self.word_length = word_length # Length of the word chosen
        self.word = self.get_word() # Get a random word from the word bank
        self.guesses = [] # Empty list for each game to store guesses and secret code
        self.status = "playing" 
        self.score = 0 # Initialize score for each game
        self.is_new_game = True # Bool to check if the game is new or not

    def get_word(self):
        """ Fetches a word from the word bank """
        with open("wordle-words.txt", "r") as file: # Open the word bank file to get a random word
            wordlist = [word.strip().lower() for word in file if len(word.strip()) == self.word_length] # Read words from wordbank into list and filter words by length
        return random.choice(wordlist) if wordlist else None # Get a random word from the wordlist using random package
    
    def check_guess(self, guess):
        """ Checker function to see if the user guess is valid """
        return len(guess) == self.word_length and guess.isalpha() # Checks if guess is valid
    
    def check_win(self, guess):
        """ Checker function to see if user guess was correct """
        return guess == self.word # returns True if guess is correct, False if incorrect
    
    def check_loss(self):
        """ Checker function to see if user has used up all of his attempts """
        return self.attempts == 0 # If user has no guesses left returns True else False and he can keep playing
    
    def give_feedback(self, guess): # We will use a different feedback system
        """ Function to create a secret code string that acts as a hint for the user to guess the word """
        feedback = "" # Initialize feedback
        for i, letter in enumerate(guess): # And then we iterate over the guess
            if letter == self.word[i]:  # If the letter is in the right place add "C" to feedback string
                feedback += "C" 
            elif letter in self.word: # If letter is not in the right place but in the correct word, adds "c" to feedback string
                feedback += "c"
            else: # If neither of those then letter is not in the correct word so add "-" to the feedback string
                feedback += "-"
        return feedback
    
    def print_gameboard(self):
        """ Function to show previous user guesses, hints and attempts left """
        print("Attempts Left:", self.attempts)
        for i, guess in enumerate(self.guesses, start=1): # We will only print the guesses by the user 
            print(f"Guess {i}: {guess} - HINT: {self.give_feedback(guess)}") # And the feedback for each guess

    def game_instructions(self):
        """ Function to print out the instructions for the game, including the length of the correct word and attempts to guess it """

        print("Welcome to Wordle!")
        print(f"The goal of the game is to guess the {self.word_length} letter word in {self.attempts} attempts.")
        print("After each guess, you will receive feedback on the letters you guessed.")
        print("If a letter is correct and in the correct position, it will be marked with a 'C'.")
        print("If a letter is correct but in the wrong position, it will be marked with a 'c'.")
        print("If a letter is incorrect, it will be marked with a '-'.")
        print("Good luck!")

    def get_score(self):
        """ Function creates a score for each game, rewards you for using fewer attempts to guess and choosing longer words"""
        penalty_for_wrong_guesses = (self.max_attempts - self.attempts) * 5 # Penalty for wrong guesses
        bonus_for_word_length = self.word_length * 10 # Bonus for word length
        streak_bonus = 0 # Bonus for streak
        total_score = 100 - penalty_for_wrong_guesses + bonus_for_word_length + streak_bonus # Total score
        return max(total_score, 0) # Return the total score, if it is negative return 0

    def play_round(self):
        """ Main function to play the game, uses everything together to make Wordle """
        self.game_instructions() # Starts off by displaying the game instructions to the user
        while self.status == "playing" and self.attempts > 0: # while loop will continue until the user wins or loses
            guess = input(f"Enter a {self.word_length} letter guess: ").lower() # Gets the user guess for the word, lower() to nullify capitalization
            if not self.check_guess(guess): # And it will check if the guess is valid
                print(f"Invalid guess, please enter a {self.word_length} letter word.") # If guess was not valid it does not take an attempt but asks for another guess instead
                continue
            self.guesses.append(guess) # If the guess is valid, it will be added to the list of guesses and the game goes on
            self.attempts -= 1
            if self.check_win(guess): # Check to see if the guessed word was correct
                self.status = "win" # If so they win
                self.score = self.get_score()
                print("Congratulations, you won! Your score is:", self.score)
                break
            elif self.check_loss(): # Check to see if they they used up all their attempts
                self.status = "lost"
                print("You lost, the word was:", self.word) # If they lost display the correct word
                break
            self.print_gameboard() # If user has not won or lost print the gameboard, guess, hint and attempts left

    def add_word_to_file():
        """ Function to let the user add words to the word bank """
        word = input("Enter a letter word: ").strip().lower() # Here we will add a word to the file and strip it and make it lowercase
        try:
            with open("wordle-words.txt", "r+") as file:
                words = [line.strip() for line in file] # Get all the words from the current wordbank into a list
                if word in words: # If the word the user chose to input is already in the word bank do nothing and give error statement
                    print("Word already exists in file.") 
                else:
                    file.seek(0, 2) # Here we are moving the cursor to the end of the file and checking if the word is in the file
                    file.write(f"{word}\n") # Put the word in the word bank
                    print(f"{word} added to file.")
        except FileNotFoundError: # Error check if wordbank does not exist
            with open("wordle-words.txt", "w") as file:
                file.write(f"{word}\n")
                print(f"{word} added to file.")

    def remove_word_from_file():
        """ Function to remove words from the word bank """
        word = input("Enter a word to remove: ").lower().strip() # User inputs the word he wants to remove
        try:
            with open("wordle-words.txt", "r") as file:
                words = file.readlines() 
            with open("wordle-words.txt", "w") as file:
                if f"{word}\n" not in words: # Check if the word is in the word bank, if not give error statement
                    print(f"{word} was not found in the word bank.")
                else: # If the word was in the word bank, remove it
                    for line in words:
                        if line.strip().lower() != word:
                            file.write(line)
                    print(f"Removed {word} from the word bank.")
        except FileNotFoundError: # Error check if wordbank does not exist
            print("Word bank file not found.")

    def manage_word_file_menu():
        """ Function that creates a menu to manage the word bank """
        while True: # Until the user chooses to exit the word bank manager menu continue
            print("\nWord Bank Management") # Instructions
            print("1. Add word to file")
            print("2. Remove word from file")
            print("3. Exit")
            choice = input("Enter choice: ") # Let user choose to either add, remove or exit the word bank manager
            if choice == "1":
                Wordle.add_word_to_file()
            elif choice == "2":
                Wordle.remove_word_from_file()
            elif choice == "3":
                break
            else: # Error check for user input
                print("Invalid choice, please enter a valid choice.")

class User:
    """ User class to save profiles between games """
    def __init__(self, name): # Add some stats for the user
        self.name = name # Name of user
        self.games = [] # Games the user has played
        self.high_score = 0 # High score of user
        self.total_score = 0 # Total score of user 
        self.wins = 0 # Total wins of user
        self.losses = 0 # Total losses of user
    
    # We add some methods to count the total score, high score, wins and losses
    def count_total_score(self):
        """ Function to count the total score of the games the user has played """
        return sum([game.score for game in self.games]) 
    
    def count_high_score(self):
        """ Function to get the best possible score the user has gotten from his games """
        return max([game.score for game in self.games])
    
    def count_wins(self):
        """ Function that counts how many games the user has won """
        return sum([1 for game in self.games if game.status == "win"])
    
    def count_losses(self):
        """ Function that counts how many games the user has lost """
        return sum([1 for game in self.games if game.status == "lost"])
    
    # We add some methods to add a game, add a game result, save stats, load stats, load user games, save user games and user history
    def add_game(self, game):
        """ Function that adds the current game to the user profile """
        self.games.append(game)

    def add_game_result(self, game):
        """ Function that adds the current games results to the user profile """
        if game.status == "win": # Add either a loss or a win to the user profile
            self.wins += 1
        else:
            self.losses += 1
        self.total_score += game.score # Add the score of the game to the total score of the user
        self.high_score = max(self.high_score, game.score)

    def save_stats(self):
        """ Function that saves the user stats to a text document, saving it for later game sessions """
        with open("stats.txt", "a") as file: 
            file.write(f"{self.name}, {self.wins}, {self.losses}, {self.total_score}, {self.high_score}\n") # Write the stats into the stats file

    def save_user_games(self):
        """ Function Appends new games to the users.txt file """
        with open("users.txt", "a") as file:
            for game in self.games:
                if game.is_new_game:  # Check if the game is marked as new
                    game_result = f"{self.name}, {game.word}, {game.status}, {game.attempts}" # Saves the information we need from each new game
                    file.write(game_result + "\n")
                    game.is_new_game = False  # Mark the game as saved, so that it wont add it again later

    def load_stats(self):
        """ Function loads the specified user stats """
        try:
            with open("stats.txt", "r") as file:
                for line in file:
                    name, wins, losses, total_score, high_score = line.strip().split(",")
                    if name == self.name: # Only add the stats if the user that is playing has played before and has a game history
                        self.wins = int(wins)
                        self.losses = int(losses)
                        self.total_score = int(total_score)
                        self.high_score = int(high_score)
                        break
        except FileNotFoundError:
            print("Stats file not found.")

    def load_user_games(self, name):
        """Function to load the previously saved user games into a new game session."""
        user_found = False  # Bool to see if user is in the document
        try:
            with open("users.txt", "r") as file:
                for line in file:  # Reads the users previous games into the user profile to continue playing
                    line_name, word, status, attempts = line.strip().split(",")
                    if line_name == name:
                        user_found = True
                        game = Wordle(int(attempts), len(word))  # initialize a game instance with the relevant attempts and word length
                        game.word = word
                        game.status = status.strip()
                        game.attempts = int(attempts)
                        game.is_new_game = False  # Make sure the game wont be saved again
                        self.games.append(game)
            if user_found:
                print(f"Welcome back {name}!")
            else:
                print(f"Welcome {name}!")
        except FileNotFoundError:  # Error check if file does not exist
            print("User file not found.")

    def user_history(self):
        """ Function to check a specific users history """
        try:
            with open("users.txt", "r") as file:
                for line in file:
                    name, word, status, attempts = line.strip().split(",")
                    if name == self.name: # After loading in the variables display the stats for the specified user
                        print(f"Name: {name}, Word:{word}, Status:{status}, Attempts:{attempts}")
        except FileNotFoundError:
            print("User file not found.")
    
def get_word_length():
    """ Function to get the word length from the user """
    while True: # While loop to ensure user will pick a word between 3 and 9
        try:
            word_length = int(input("Choose the length of the word you want to guess between 3 and 9: ")) # User chooses the length of the word he wants to guess
            if word_length < 3 or word_length > 9:
                print("Invalid input. Please enter a number between 3 and 10.")
                return get_word_length()
            else:
                return word_length
        except ValueError:
            print("Invalid input. Please enter a number.")
            return get_word_length()
        
def get_attempts():
    """ Function to get the number of attempts from the user """
    while True: # While loop to ensure user will pick a number of attempts between 3 and 10
        try:
            attempts = int(input("Choose the number of attempts you want to have between 3 and 10: ")) # User chooses the number of attempts he wants to have
            if attempts < 3 or attempts > 10:
                print("Invalid input. Please enter a number between 1 and 10.")
                return get_attempts() # If user does anything but input a number between 3 and 10 it will prompt another input
            else:
                return attempts
        except ValueError:
            print("Invalid input. Please enter a number.")
            return get_attempts()
    
def play_game(user):
    """ Function adds together the neccesary components to play the game """
    word_length = get_word_length() # Get the word length from the user
    user_attempts = get_attempts() # Get the number of attempts from the user
    game = Wordle(user_attempts, word_length) # Initialize the game
    game.play_round() # Play the game
    user.add_game(game) # Add the game to the user's game history
    user.add_game_result(game) # Update user's stats based on the game result


def play_game_loop(user): 
    """This function enables the user to play again without going back to the menu screen"""
    while True: # While loop to ensure the user only inputs either y or n
        play_game(user)

        play_again = input("Do you want to play again? (y/n): ") # Ask the user if he wants to play again
        if play_again not in ['y', 'Y', 'n', 'N']:
            print("invalid input, please enter y or n")
            continue

        if play_again == 'n' or play_again == 'N':
            user.save_user_games()
            break

def main():
    """ Main game function that enables the user to play the Wordle game """
    name = input("Enter your username: ")
    user = User(name)
    user.load_user_games(name) # Load user games from file if user exists

    while True: # While loop maintains until the user decides to quit playing. Enables the user to play the game
        print("\nWordle Menu") # Instructions on how to choose your options
        print("1. Play Wordle")
        print("2. Manage Word Bank")
        print("3. View Game History")
        print("4. View Stats")
        print("5. Exit")
        choice = input("Enter choice: ")
        if choice == "1": # User decided to play Wordle
            play_game_loop(user) # Function enables the gameplay and play again functionality
        elif choice == "2": # User decided to manage the word bank
            Wordle.manage_word_file_menu()
        elif choice == "3": # User decided to check his game history
            user.user_history()
        elif choice == "4": # User decided to view his game stats
            user.load_stats() # Load user stats from file
            print(f"User: {user.name}")
            print(f"Total games played: {user.wins + user.losses}")
            print(f"Wins: {user.wins}")
            print(f"Losses: {user.losses}")
            print(f"Total Score: {user.total_score}")
            print(f"High Score: {user.high_score}")
        elif choice == "5":
            user.save_user_games()
            user.save_stats() # Save the users games since he decided to stop playing
            break
        else:
            print("Invalid choice, please enter a valid choice.")
    

if __name__ == "__main__":
    main()

