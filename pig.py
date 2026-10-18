import random

random.seed(0)


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def add_score(self, points):
        self.score += points


class Die:
    def roll(self):
        return random.randint(1, 6)

class PigGame:
    def __init__(self):
        self.players = [Player("Player 1"), Player("Player 2")]
        self.die = Die()
        self.current_player = 0

    def play(self):
        print("Welcome to the Pig Dice Game!")

        while True:
            player = self.players[self.current_player]
            turn_total = 0

            print(f"\n{player.name}'s turn!")
            print(f"Total score: {player.score}")

            while True:
                print(f"Turn total: {turn_total}")
                choice = input("Roll (r) or Hold (h)? ").lower()

                if choice == "r":
                    roll = self.die.roll()
                    print(f"You rolled a {roll}!")

                    if roll == 1:
                        print("You rolled a 1! You lose your turn points.")
                        break

                    turn_total += roll
                    print(f"Turn total: {turn_total}")
                    print(f"Overall score: {player.score}")

                elif choice == "h":
                    player.add_score(turn_total)
                    print(f"{player.name}'s total score: {player.score}")
                    break

                else:
                    print("Invalid choice. Enter r or h.")

            if player.score >= 100:
                print(f"\n{player.name} wins with {player.score} points!")
                break

            self.current_player = 1 - self.current_player


if __name__ == "__main__":
    game = PigGame()
    game.play()
    def roll(self):
        return random.randint(1, 6)
