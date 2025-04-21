from player import Player
from zone_loader import ZoneLoader

def main():
    print("Welcome to Veilshard: Echoes of the First Shard")
    name = input("Enter your character's name: ")
    player = Player(name)
    loader = ZoneLoader()
    current_zone = loader.load_zone("tutorial_entrance")

    while True:
        print(f"\n{current_zone['description']}")
        if "items" in current_zone:
            for item in current_zone["items"]:
                if item not in player.inventory:
                    print(f"You notice something: {item}")
        action = input("What do you do? ").lower().strip()

        if action == "look":
            print(current_zone["description"])
        elif action.startswith("move "):
            direction = action.split(" ")[1]
            if direction in current_zone["exits"]:
                next_zone_key = current_zone["exits"][direction]
                current_zone = loader.load_zone(next_zone_key)
            else:
                print("You can't go that way.")
        elif action.startswith("take "):
            item = action.split(" ", 1)[1]
            if item in current_zone.get("items", []) and item not in player.inventory:
                player.inventory.append(item)
                print(f"You take the {item}.")
            else:
                print("Nothing to take.")
        elif action == "inventory":
            print("Your inventory:", player.inventory)
        elif action == "quit":
            print("Thanks for playing!")
            break
        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()

from player import Player
from zone_loader import ZoneLoader

def main():
    print("Welcome to Veilshard: Echoes of the First Shard")
    name = input("Enter your character's name: ")
    player = Player(name)
    loader = ZoneLoader()
    current_zone = loader.load_zone("tutorial_entrance")

    while True:
        print(f"\n{current_zone['description']}")
        if "items" in current_zone:
            for item in current_zone["items"]:
                if item not in player.inventory:
                    print(f"You notice something: {item}")
        action = input("What do you do? ").lower().strip()

        if action == "look":
            print(current_zone["description"])
        elif action.startswith("move "):
            direction = action.split(" ")[1]
            if direction in current_zone["exits"]:
                next_zone_key = current_zone["exits"][direction]
                current_zone = loader.load_zone(next_zone_key)
            else:
                print("You can't go that way.")
        elif action.startswith("take "):
            item = action.split(" ", 1)[1]
            if item in current_zone.get("items", []) and item not in player.inventory:
                player.inventory.append(item)
                print(f"You take the {item}.")
            else:
                print("Nothing to take.")
        elif action == "inventory":
            print("Your inventory:", player.inventory)
        elif action == "quit":
            print("Thanks for playing!")
            break
        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()
