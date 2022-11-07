# code a rock paper scissor game
# Code for 1 or 2 players
# Code comparison

import random

class RockPaperScissor:
    def __init__(self, roundsToWin):
        self.picks = ['Rock', 'Paper', 'Scissors']
        self.results = ['Win', 'Lose', 'Draw']
        self.score = [0, 0]
        self.roundsToWin = roundsToWin
        self.currentRound = 1

    def compare(self, p1, p2):
        self.printAndIncreRounds()
        self.printPicks(p1, p2)
        if p1 == p2:
            print(self.results[2])
        elif p2 - p1 == 1 or p2 - p1 == -2:
            self.score[1] += 1
            print(self.results[1])
        else:
            self.score[0] += 1
            print(self.results[0])

    def checkWinCondition(self):
        if self.score[0] == self.roundsToWin:
            self.resetScore()
            print("You Win!")
        elif self.score[1] == self.roundsToWin:
            self.reset()
            print("You Lost!")
        else: 
            print("Current score: " + str(self.score[0]) + " : " + str(self.score[1]))

    def play(self, pick):
        self.compare(pick, random.randint(0, 2))
        self.checkWinCondition()
        print()

    def reset(self):
        self.score = [0, 0]
        self.currentRound = 1

    def printPicks(self, p1, p2):
        print(self.picks[p1] + " vs " + self.picks[p2])

    def printAndIncreRounds(self):
        print("Round " + str(self.currentRound))
        self.currentRound += 1


game = RockPaperScissor(3)
for i in range(7):
    game.play(1)