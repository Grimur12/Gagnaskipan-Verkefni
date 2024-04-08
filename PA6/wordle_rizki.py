import random

class Wordle:
    def __init__(self):
        self.word = self.get_word()
        self.attempts = 5
        self.guesses = []
        self.status = "playing"

    def get_word(self):
        with open("wordle-5letter-words.txt", "r") as file:
            wordlist = [word.strip().lower() for word in file]
        return random.choice(wordlist)
    
    def check_guess(self, guess):
        if len(guess) != 5:
            return False
        return True
    
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
    
    def play_round(self):
        while self.status == "playing":
            guess = input("Enter a 5 letter guess: ").lower()
            if not self.check_guess(guess):
                print("Invalid guess, please enter a 5 letter word.")
                continue
            self.guesses.append(guess)
            self.attempts -= 1
            feedback = self.give_feedback(guess)
            print(f"Feedback: {feedback}")
            if self.check_win(guess):
                self.status = "win"
            elif self.check_loss():
                self.status = "lost"
            self.print_gameboard()
        if self.status == "win":
            print("Congratulations! You won!")
        else:
            print("You lost! The word was:", self.word)
        print("Guesses:")
        for i, guess in enumerate(self.guesses):
            print(f"Guess {i+1}: {guess}")
        print("Feedback:")
        for i, guess in enumerate(self.guesses):
            print(f"Guess {i+1}: {self.give_feedback(guess)}")

class User:
    def __init__(self, name):
        self.name = name
        self.games = []
    
    def add_game(self, game):
        self.games.append(game)
    
    def get_score(self):
        score = 0
        for game in self.games:
            if game.status == "win":
                score += game.attempts
        return score    
    
    def display_history(self):
        print(f"Game history for {self.name}:")
        top_score = 0
        top_game = None
        for i, game in enumerate(self.games):
            score = game.attempts
            print(f"Game {i+1}: Score - {score}")
            if score > top_score:
                top_score = score
                top_game = game
        if top_game:
            print("Top scoring game:")
            print(f"Word: {top_game.word}")
            top_game.print_gameboard()
    
    def save_user(self):
        with open("users.txt", "a") as file:
            file.write(f"{self.name}\n")
            for game in self.games:
                file.write(f"{game.word},{game.status},{game.attempts}\n")

    def register_user(self):
        with open("users.txt", "r") as file:
            users = [line.strip() for line in file]
        if self.name in users:
            return False
        return True
    
    def load_user(self):
        with open("users.txt", "r") as file:
            users = [line.strip() for line in file]
        if self.name not in users:
            return False
        return True
    
    def load_games(self):
        with open("users.txt", "r") as file:
            lines = file.readlines()
        games = []
        for i, line in enumerate(lines):
            if line.strip() == self.name:
                word, status, attempts = lines[i+1].strip().split(",")
                game = Wordle()
                game.word = word
                game.status = status
                game.attempts = int(attempts)
                self.games.append(game)

    def save_games(self):
        with open("users.txt", "r") as file:
            lines = file.readlines()
        with open("users.txt", "w") as file:
            for line in lines:
                if line.strip() == self.name:
                    file.write(f"{self.name}\n")
                    for game in self.games:
                        file.write(f"{game.word},{game.status},{game.attempts}\n")
                else:
                    file.write(line)

    

        
def main():
    user = input("Enter your username: ")
    user = User(user)
    if not user.load_user():
        print("User not found, creating new user.")
        if not user.register_user():
            print("User already exists.")
            return
    else:
        user.load_games()
    user.display_history()

    play = input("Do you want to play a game? (Y/N): ").lower()
    if play == "y":
        game = Wordle()
        game.play_round()
        user.add_game(game)
        user.save_games()
        user.display_history()
    user.save_user()



if __name__ == "__main__":
    main()

            