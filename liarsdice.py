import random

class Player:
    def __init__(self, is_human=True):
        self.is_human = is_human
        self.dice_count = 5  # Initial number of dice
        self.dice = []  # Player's dice

    def roll_dice(self):
        self.dice = [random.randint(1, 6) for _ in range(self.dice_count)]
    
    def lose_die(self):
        self.dice_count -= 1

    def bid(self, current_bid):
        if self.is_human:
            return self._human_bid(current_bid)
        else:
            return self._cpu_bid(current_bid)

    def _human_bid(self, current_bid):
        print(f"Your dice: {self.dice}")
        print(f"Current bid: {current_bid}")
        while True:
            bid = input("Enter your bid (quantity value): ")
            bid = bid.split()
            if len(bid) != 2 or any(not 1 <= int(val) <= 6 for val in bid):
                print("Invalid input. Please enter two numbers separated by a space.")
                continue
            try:
                quantity = int(bid[0])
                value = int(bid[1])
                if current_bid is None or quantity > current_bid[0] or (quantity == current_bid[0] and value > current_bid[1]):
                    return (quantity, value)
                else:
                    print("Your bid must be higher than the current bid.")
            except ValueError:
                print("Invalid input. Please enter two numbers separated by a space.")

    def _cpu_bid(self, current_bid):
        if current_bid is None:
            # If no bid has been made yet, generate a random bid
            quantity = random.randint(1, self.dice_count)
            value = random.randint(1, 6)
        else:
            # Generate a bid based on the current bid
            quantity, value = current_bid
            if random.random() < 0.5:
                quantity += random.randint(1, 2)
            else:
                value += random.randint(1, 2)
                if value > 6:
                    value = 6
            if quantity > self.dice_count:
                quantity = self.dice_count
        new_bid = (quantity, value)
        
        print(f"New bid: {new_bid}")
        return new_bid


    def call_bluff(self, current_bid, total_count):
        quantity, value = current_bid
        print(f"There are a total of {total_count} {value}s")
        if quantity > total_count:
            return True
        else:
            return False
    
    def take_turn(self, current_bid):
        if self.is_human:
            return self._human_turn(current_bid)
        else:
            return self._cpu_turn(current_bid)

    def _human_turn(self, current_bid):
        print(f"Your dice: {self.dice}")
        print(f"Current bid: {current_bid}")
        while True:
            action = input("Choose your action (bid, call): ").lower()
            if action == 'bid':
                return self._human_bid(current_bid)
            elif action == 'call':
                return 'call'
            else:
                print("Invalid action. Please choose 'bid' or 'call'.")
    
    def _cpu_turn(self, current_bid):
        action = random.choice(['bid', 'call'])
        if action == 'bid':
            print("CPU chose to raise the bid")
            return self._cpu_bid(current_bid)
        else:
            print("CPU chose to call")
            return 'call'


def play_liars_dice(num_players=2):
    players = [Player(is_human=(i == 0)) for i in range(num_players)]

    while True:
        for player in players:
            player.roll_dice()
            print(player.dice)

        current_bid = None

        while True:
            for player in [p for p in players if p.dice_count > 0]:  # Iterate over active players only
                print(f"\nPlayer {players.index(player) + 1}'s turn:")
                
                if current_bid is None:
                    # First turn, ask for a bid
                    action = player.bid(current_bid)
                else:
                    # Subsequent turns, give the choice of either a bid or a call
                    action = player.take_turn(current_bid)

                if action == "call":
                    total_count = sum([p.dice.count(current_bid[1]) for p in players])
                    result = player.call_bluff(current_bid, total_count)
                    if result:
                        # Player getting called out loses a die
                        players[(players.index(player) - 1) % num_players].lose_die()
                        print(f"Player {(players.index(player) - 1) % num_players + 1} loses a die")
                    else:
                        # Player who called loses a die
                        player.lose_die()
                        print(f"Player {players.index(player) + 1} loses a die")
                    break
                else:
                    current_bid = action
            
            active_players = [p for p in players if p.dice_count > 0]
            if len(active_players) == 1:
                print(f"\nPlayer {players.index(active_players[0]) + 1} wins!")
                return players.index(active_players[0]) + 1
            
            # Start new round if someone called
            if action == "call":
                break


# Main game loop
while True:
    num_players = int(input("Enter number of players: "))
    play_liars_dice(num_players)

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break
