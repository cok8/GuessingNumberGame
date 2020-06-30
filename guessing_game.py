class GuessNumber:
    def __init__(self, number, min = 0, max = 100):
        self.number = number
        self.min  = min
        self.max = max
        self.guess_amount = 1

    def get_guess(self):
        guess = input(f"Try number between {self.min} and {self.max}: ")
        next_step = False

        if self.valid_number(guess):
            return int(guess)
        else:
            print("Please enter a valid number")
            return self.get_guess()

    def valid_number(self, str_number):
        try:
            number = int(str_number)
        except:
            return False

        return self.min <= number <= self.max


    def play(self):
        game = True
        while game:
            value = self.get_guess()
            print(type(value))
            if value == self.number:
                print(f"You guessed right after {self.guess_amount} attempts")
                game = False
            elif value <= self.number:
                print("higher!")
                self.guess_amount += 1
            else:
                print("lower")
                self.guess_amount += 1


Game = GuessNumber(50)
Game.play()