import random

class Wordle:
    def __init__(self, attempts=5, word_length=5):
        self.attempts = attempts
        self.word_length = word_length
        self.word = self.get_word()
        self.guesses = []
        self.status = "playing"
        self.score = 0

    def get_word(self):
        with open("wordle-words.txt", "r") as file:
            wordlist = [word.strip().lower() for word in file if len(word.strip()) == self.word_length]
        return random.choice(wordlist) if wordlist else None
    
    def check_guess(self, guess):
        return len(guess) == self.word_length and guess.isalpha()
    
    def check_win(self, guess):
        return guess == self.word
    
    def check_loss(self):
        return self.attempts == 0
    
    def give_feedback(self, guess):
        feedback = ""
        for i, letter in enumerate(guess):
            if letter == self.word[i]:
                feedback += "C"
            elif letter in self.word:
                feedback += "c"
            else:
                feedback += "-"
        return feedback
    
    def print_gameboard(self):
        print("Attempts Left:", self.attempts)
        for i, guess in enumerate(self.guesses, start=1):
            print(f"Guess {i}: {guess} - HINT: {self.give_feedback(guess)}")

    def game_instructions(self):
        print("Welcome to Wordle!")
        print(f"The goal of the game is to guess the {self.word_length} letter word in {self.attempts} attempts.")
        print("After each guess, you will receive feedback on the letters you guessed.")
        print("If a letter is correct and in the correct position, it will be marked with a 'C'.")
        print("If a letter is correct but in the wrong position, it will be marked with a 'c'.")
        print("If a letter is incorrect, it will be marked with a '-'.")
        print("Good luck!")
    
    def play_round(self):
        self.game_instructions()
        while self.status == "playing" and self.attempts > 0:
            guess = input(f"Enter a {self.word_length} letter guess: ").lower()
            if not self.check_guess(guess):
                print(f"Invalid guess, please enter a {self.word_length} letter word.")
                continue
            self.guesses.append(guess)
            self.attempts -= 1
            feedback = self.give_feedback(guess)
            print(f"Feedback: {feedback}")
            if self.check_win(guess):
                self.status = "win"
                self.score = self.attempts * 10
                print("Congratulations, you won! Your score is:", self.score)
                break
            elif self.check_loss():
                self.status = "lost"
                print("You lost, the word was:", self.word)
                break
            self.print_gameboard()
        # for i, guess in enumerate(self.guesses):
        #     print(f"Guess {i+1}: {guess}")
        # print("Feedback:")
        # for i, guess in enumerate(self.guesses):
        #     print(f"Guess {i+1}: {self.give_feedback(guess)}")

    def add_word_to_file():
        word = input("Enter a letter word: ").strip().lower()
        try:
            with open("wordle-words.txt", "r+") as file:
                words = [line.strip() for line in file]
                if word in words:
                    print("Word already exists in file.")
                else:
                    file.seek(0, 2) 
                    file.write(f"{word}\n")
                    print(f"{word} added to file.")
        except FileNotFoundError:
            with open("wordle-words.txt", "w") as file:
                file.write(f"{word}\n")
                print(f"{word} added to file.")



    def remove_word_from_file():
        word = input("Enter a word to remove: ").lower().strip()
        try:
            with open("wordle-words.txt", "r") as file:
                words = file.readlines()
            with open("wordle-words.txt", "w") as file:
                if f"{word}\n" not in words:
                    print(f"{word} was not found in the word bank.")
                else:
                    for line in words:
                        if line.strip().lower() != word:
                            file.write(line)
                    print(f"Removed {word} from the word bank.")
        except FileNotFoundError:
            print("Word bank file not found.")

    def manage_word_file_menu():
        while True:
            print("\nWord Bank Management")
            print("1. Add word to file")
            print("2. Remove word from file")
            print("3. Exit")
            choice = input("Enter choice: ")
            if choice == "1":
                Wordle.add_word_to_file()
            elif choice == "2":
                Wordle.remove_word_from_file()
            elif choice == "3":
                break
            else:
                print("Invalid choice, please enter a valid choice.")




class User:
    def __init__(self, name):
        self.name = name
        self.games = []
        self.high_score = 0
        self.total_score = 0
        self.wins = 0
        self.losses = 0
    
    def count_total_score(self):
        return sum([game.score for game in self.games])
    
    def count_high_score(self):
        return max([game.score for game in self.games])
    
    def count_wins(self):
        return sum([1 for game in self.games if game.status == "win"])
    
    def count_losses(self):
        return sum([1 for game in self.games if game.status == "lost"])
    
    def add_game(self, game):
        self.games.append(game)

    def add_game_result(self, game):
        if game.status == "win":
            self.wins += 1
        else:
            self.losses += 1
        self.total_score = self.count_total_score()
        self.high_score = self.count_high_score()

    def save_stats(self):
        with open("stats.txt", "w") as file:
            file.write(f"{self.name}, {self.wins}, {self.losses}, {self.total_score}, {self.high_score}\n")

    def load_stats(self):
        try:
            with open("stats.txt", "r") as file:
                line = file.readline().strip()
                parts = line.split(",")
                if len(parts) == 5:
                    self.name, wins, losses, total_score, high_score = parts
                    self.wins = int(wins)
                    self.losses = int(losses)
                    self.total_score = int(total_score)
                    self.high_score = int(high_score)
                else:
                    raise ValueError("Incorrect file format")
        except FileNotFoundError:
            print("Stats file not found.")
        except ValueError as e:
            print(f"Error loading stats: {e}")



    def load_user_games(self):
        try:
            with open("users.txt", "r") as file:
                for line in file:
                    self.name, word, status, attempts = line.strip().split(",")
                    game = Wordle(int(attempts))
                    game.word = word
                    game.status = status
                    game.attempts = int(attempts)
                    self.games.append(game)
        except FileNotFoundError:
            print("User file not found.")

    def save_user_games(self):
        with open("users.txt", "w") as file:
            for game in self.games:
                file.write(f"{self.name}, {game.word}, {game.status}, {game.attempts}\n")

    def user_history(self):
        if not self.games:
            print("No games played yet.")
            return
        print("Game history for", self.name)
        for game in self.games:
            status = "Won" if game.status == "win" else "Lost"
            print(f"User: {self.name} - Word: {game.word} - Status: {status} - Attempts remaining: {game.attempts}")

    

        
def main():
    user = input("Enter your username: ")
    user = User(user)
    user.load_user_games() # Load user games from file if user exists

    while True:
        print("\nWordle Menu")
        print("1. Play Wordle")
        print("2. Manage Word Bank")
        print("3. View Game History")
        print("4. View Stats")
        print("5. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            while True:
                try:
                    play = input("Choose the length of the word you want to guess: ")
                    word_length = int(play)
                    # Ensure word_length is within a reasonable range
                    word_length = max(3, min(word_length, 10))
                    break  # Exit the loop if the input is successfully converted
                except ValueError:
                    print("Invalid input. Please enter a number.")

            game = Wordle(word_length=word_length)
            game.play_round()
            user.add_game(game)
            user.add_game_result(game)
            user.save_stats()
        elif choice == "2":
            Wordle.manage_word_file_menu()
        elif choice == "3":
            user.user_history()
        elif choice == "4":
            user.load_stats()
            print(f"User: {user.name}")
            print(f"Wins: {user.wins}")
            print(f"Losses: {user.losses}")
            print(f"Total Score: {user.total_score}")
            print(f"High Score: {user.high_score}")
        elif choice == "5":
            user.save_user_games()
            break
        else:
            print("Invalid choice, please enter a valid choice.")
        user.save_user_games()
        user.save_stats()
    



if __name__ == "__main__":
    main()

            