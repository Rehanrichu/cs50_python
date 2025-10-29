# project.py

def show_intro():
    print("🤖 Welcome to AI Dungeon Explorer!")
    print("Your goal is to collect 5 AI knowledge tokens from different rooms by solving puzzles.")
    print("Type 'help' to see available actions.\n")

def get_player_action():
    return input("What do you want to do? ").lower().strip()

def north_puzzle():
    print("what is 45*45 ?")
    answer = input("Your answer: ")
    return answer.strip() == "2025"

def south_puzzle():
    import random
    number = random.randint(1,5)
    print("Guess the number between 1 and 5 to get the token!")
    guess = input("Your guess: ")
    return guess.strip() == str(number)

def east_puzzle():
    print("Choose the correct AI field to get the token: ML, NLP, Robotics")
    answer = input("Your answer: ").lower()
    return answer == "ml"

def west_puzzle():
    print("Rearrange the letters: 'egondnu' to form a meaningful phrase.")
    answer = input("Your answer: ").lower()
    return answer == "dungeon"

def central_puzzle():
    print("who is the father of mathematics?")
    answer = input("Your answer: ").lower()
    return answer == "archimedes"

def update_state(action, state):
    rooms = ["north","south","east","west","central"]
    if action == "help":
        print("Available actions: move north/move south/move east/move west/move central, inspect, collect, quit")
    elif action.startswith("move"):
        direction = action.split()[1] if len(action.split())>1 else ""
        if direction in rooms:
            state['location'] = direction
            print(f"You moved {direction}.")
        else:
            print("You can't go that way.")
    elif action == "inspect":
        loc = state['location']
        if loc not in state['inventory']:
            print("You see a puzzle that guards a token here!")
        else:
            print("Nothing interesting here.")
    elif action == "collect":
        loc = state['location']
        if loc in state['inventory']:
            print("You already collected the token here.")
            return
        success = False
        if loc == "north": success = north_puzzle()
        elif loc == "south": success = south_puzzle()
        elif loc == "east": success = east_puzzle()
        elif loc == "west": success = west_puzzle()
        elif loc == "central": success = central_puzzle()
        if success:
            state['inventory'].append(loc)
            print(f"🎉 Token collected from {loc}! Total tokens: {len(state['inventory'])}/5")
        else:
            print("❌ Puzzle failed. Try again.")
    elif action == "quit":
        state['game_over'] = True
        print("Thanks for playing!")
    else:
        print("Invalid action. Type 'help' for options.")

def main():
    show_intro()
    state = {
        "location":"central",
        "inventory":[],
        "game_over":False
    }
    while not state['game_over']:
        action = get_player_action()
        update_state(action,state)
        if len(state['inventory'])>=5:
            print("\n🏆 Congratulations! You collected all 5 AI knowledge tokens and won the game!")
            break

if __name__=="__main__":
    main()
