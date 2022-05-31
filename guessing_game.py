class GuessingGame():

    def __init__(self, answer):
        self.answer = answer
        
        
    def guess(self, user_guess):
        self.user_guess = user_guess
        if user_guess == self.answer:
            return "Correct!"
        elif user_guess > self.answer:
            return "high!"
        else: return "low!"
    
    
    
    def solved(self):
        # print(self.user_guess)
        if self.user_guess == self.answer:
            return f"Your last guess {self.user_guess} was {self.guess(self.user_guess)}."
        else:
            return f"Your last guess {self.user_guess} was {self.guess(self.user_guess)}."

game = GuessingGame(10)
print(game.guess(4))
print(game.solved())