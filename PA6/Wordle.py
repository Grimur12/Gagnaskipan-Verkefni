import random

class Wordle:

    def __init__(self, wordlist):
        self.wordlist = wordlist
        self.word = self.getword()
        self.attempts = 5
        self.status = None
        self.guesses = [] # Setja hérna orðin sem notandi giskar og kóðann tengdann við orðið til að prenta út seinna

    def getword(self):
        # get a random numnber from 0 to length of worlde word list and index that number to get a random 5 letter word
        index = random.randint(0,len(self.wordlist) - 1)
        return self.wordlist[index]

    def guess(self, guess_word):
        # Guesses
        if len(guess_word) != 5:
            print("Your guess needs to be 5 letters")
            return
        
        self.attempts -= 1
        result = self.compare(guess_word)
        self.guesses.append((guess_word, result))

        if result == "CCCCC":
            self.win()
        elif self.attempts == 0:
            self.loss()

    def compare(self, guess_word):
        """ If a letter is in the right place we get an uppercase C, 
        if a letter is in the real word but at another place we get a lowercase c, 
        if a letter is not in the real word we get a dash "-" """
        feedback_str = ""

        for i in range(len(self.word)):
            if guess_word[i] == self.word[i]:
                feedback_str += "C"
            elif guess_word[i] in self.word:
                feedback_str += "c"
            else:
                feedback_str += "-"
        
        return feedback_str

    def win(self):
        # Ehv meira
        self.status = "win"
        print("You won!, The word was:", self.word)
    
    def loss(self):
        # Ehv meira
        self.status = "lost"
        print("You did not correctly guess the word in 5 attempts. The word was:", self.word)

    def initialize_game(self):
        print("You will get 5 attempts to guess a 5-letter word.")
        print("After each guess, you will get hints about whether a letter is in the right place or not.")
        print("An uppercase 'C' means a correct letter in the correct place.")
        print("A lowercase 'c' means a correct letter but in the wrong place.")
        print("A dash '-' means a wrong letter.")

    def print_gameboard(self):
        print("Attempts Left:",self.attempts)
        for i, (guess, feedback) in enumerate(self.guesses, start=1):
            print(f"Guess {i}: {guess} - HINT: {feedback}")

    def get_score(self):
        # Fær stig fyrir að ná orðinu á akveðnum attempts, kanski breyta siðar
        return 10 * (5 - self.attempts)

    def get_status(self):
        if self.status == "win":
            return 1
        if self.status == "lost":
            return 0
        
class User:
    def __init__(self, name):
        self.name = name
        self.games = []

    def add_game(self, game):
        self.games.append(game)

    def display_history(self):
        print(f"Game history for {self.name}:")
        top_score = 0
        top_game = None
        for i, game in enumerate(self.games):
            score = game.get_score()
            print(f"Game {i+1}: Score - {score}")
            if score > top_score:
                top_score = score
                top_game = game
        if top_game:
            print("Top scoring game:")
            print(f"Word: {top_game.word}")
            top_game.print_gameboard()
    
## Spila leikinn
def play_game():
    with open("wordle-5letter-words.txt", "r") as file:
        wordlist = [word.strip().lower() for word in file]

    users = load_users()

    user = select_user(users)

    game = Wordle(wordlist)
    game.initialize_game()

    while game.status is None:
        guess_word = input("Enter your guess: ").strip().lower()
        game.guess(guess_word)
        game.print_gameboard()

    user.add_game(game)
    status = game.get_status()
    score = game.get_score()
    save_users(users, game.word, status, score)

    play_again = input("Do you wish to play again? (Y/N): ").strip().lower()

    if play_again == "y":
        play_game()
    elif play_again == "n":
        print("Thank you for playing Wordle!")

def load_users():
    try:
        with open("users.txt", "r") as file:
            lines = file.readlines()
            users = {}
            for line in lines:
                name = line.strip()
                users[name] = User(name)
    except FileNotFoundError:
        users = {}
    return users

def save_users(users, word, status, score):
    # Þarf að bæta við word, status, score
    with open("users.txt", "w") as file:
        for user in users.values():
            file.write(user.name + "\n")

def select_user(users):
    print("List of existing users:")
    for name, user in users.items():
        print(f"{name}: {len(user.games)} games played")
    print("Create a new user:")
    
    username = input("Enter your username: ").strip().lower()
    if username in users:
        print(f"Welcome back, {username}!")
        return users[username]
    else:
        print(f"Creating new profile for {username}.")
        user = User(username)
        users[username] = user
        return user


if __name__ == "__main__":
    play_game()
