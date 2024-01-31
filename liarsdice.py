import random

def roll_dice(num_dice):
    return [random.randint(1, 6) for _ in range(num_dice)]

def count_dice(dice, value):
    return dice.count(value)

def print_dice(dice):
    print("Your dice:", dice)

def print_bid(current_bid):
    print("Current bid:", current_bid)

def player_bid(current_bid):
    print_bid(current_bid)
    while True:
        bid = input("Enter your bid (quantity value): ")
        bid = bid.split()
        if len(bid) != 2 or any(not 1 <= int(val) <= 6 for val in bid):
            print("Invalid input. Please enter two numbers separated by a space.")
            continue
        try:
            quantity = int(bid[0])
            value = int(bid[1])
            if quantity > current_bid[0] or (quantity == current_bid[0] and value > current_bid[1]):
                return (quantity, value)
            else:
                print("Your bid must be higher than the current bid.")
        except ValueError:
            print("Invalid input. Please enter two numbers separated by a space.")

def cpu_bid(current_bid, num_dice):
    quantity, value = current_bid
    if random.random() < 0.5:
        quantity += random.randint(1, 2)
    else:
        value += random.randint(1, 2)
        if value > 6:
            value = 6
    if quantity > num_dice:
        quantity = num_dice
    return (quantity, value)

def player_turn(player_dice, num_dice, current_bid):
    print_dice(player_dice)
    print_bid(current_bid)
    while True:
        action = input("Choose your action (call, raise): ").lower()
        if action == "call":
            return "call"
        elif action == "raise":
            return player_bid(current_bid)
        else:
            print("Invalid action. Please choose from call or raise.")

def cpu_turn(num_dice, current_bid):
    action = random.choice(["call", "raise"])
    if action == "raise":
        new_bid = cpu_bid(current_bid, num_dice)
        print("CPU raised the bid to {} {}s.".format(new_bid[0], new_bid[1]))
        return new_bid
    else:
        return action

def call_bluff(player_dice, cpu_dice, current_bid):
    quantity, value = current_bid
    total_count = count_dice(player_dice, value) + count_dice(cpu_dice, value)
    print(f"There are a total of {total_count} {value}s")
    if quantity > total_count:
        return True 
    else:
        return False

def play_liars_dice():
    num_dice = 5
    player_dice_count = num_dice
    cpu_dice_count = num_dice

    while True:
        # Players roll their dice
        player_dice = roll_dice(player_dice_count)
        cpu_dice = roll_dice(cpu_dice_count)

        # Initialize current bid for the round
        current_bid = (1, 1)  # Initial bid

        print_dice(player_dice)
        print(f"CPU dice: {cpu_dice}")
        print_bid(current_bid)

        # Player and CPU take turns until someone calls
        while True:
            # Player's turn
            print("\nYour turn:")
            action = input("Choose your action (raise, call): ").lower()
            if action == "call":
                result = call_bluff(player_dice, cpu_dice, current_bid)
                if result == True:
                    print("You called bluff successfully. CPU loses a die")
                    cpu_dice_count -= 1
                else:
                    print("You called bluff incorrectly. You lose a die")
                    player_dice_count -= 1
                break
            elif action == "raise":
                current_bid = player_bid(current_bid)
            else:
                print("Invalid action. Please choose from raise or call.")

            # CPU's turn
            print("\nCPU's turn:")
            action = cpu_turn(cpu_dice_count, current_bid)
            if action == "call":
                result = call_bluff(player_dice, cpu_dice, current_bid)
                if result == True:
                    print("CPU called bluff successfully. You lose a die")
                    player_dice_count -= 1
                else:
                    print("CPU called bluff incorrectly. CPU loses a die")
                    cpu_dice_count -= 1
                break
            else:
                current_bid = action

        # Check for end of game
        if player_dice_count == 0:
            return "cpu"
        elif cpu_dice_count == 0:
            return "player"
        
# Main game loop
while True:
    winner = play_liars_dice()
    if winner == "player":
        print("Congratulations! You win!")
    else:
        print("CPU wins! Better luck next time.")
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break