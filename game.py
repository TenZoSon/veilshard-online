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

# player.py

class Player:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.inventory = []
        self.skills = []
        self.reputation = {}
        self.journal = {
            "quests": [],
            "lore": [],
            "clues": []
        }

    def gain_reputation(self, faction, amount):
        self.reputation[faction] = self.reputation.get(faction, 0) + amount

    def add_journal_entry(self, category, text):
        if category in self.journal:
            self.journal[category].append(text)
# factions/faction_system.py

class Faction:
    def __init__(self, name):
        self.name = name
        self.reputation = 0
        self.rank = "Neutral"

    def gain_reputation(self, amount):
        self.reputation += amount
        self.update_rank()

    def update_rank(self):
        if self.reputation >= 200:
            self.rank = "Ascendant"
        elif self.reputation >= 150:
            self.rank = "Bound"
        elif self.reputation >= 100:
            self.rank = "Trusted"
        elif self.reputation >= 50:
            self.rank = "Known"
        else:
            self.rank = "Neutral"

    def show_status(self):
        return f"{self.name} Rep: {self.reputation} ({self.rank})"

# journal/journal.py

class Journal:
    def __init__(self, player_name):
        self.player = player_name
        self.entries = {
            "lore": [],
            "quests": [],
            "clues": []
        }

    def add_entry(self, entry_type, text):
        if entry_type in self.entries:
            self.entries[entry_type].append(text)
            print(f"{entry_type.title()} entry added: {text}")

    def display(self, entry_type):
        if entry_type in self.entries:
            print(f"=== {self.player}'s {entry_type.title()} ===")
            for i, entry in enumerate(self.entries[entry_type], 1):
                print(f"{i}. {entry}")


# zone_loader.py

class ZoneLoader:
    def __init__(self):
        self.zones = {
            "tutorial_entrance": {
                "description": "You awaken in a strange cavern where echoes whisper your name. There’s a faint light to the north.",
                "exits": {"north": "shattered_path"},
                "items": ["cracked stone tablet"]
            },
            "shattered_path": {
                "description": "Fragments of old runes glow softly beneath your feet. A gust of wind howls from the east.",
                "exits": {"south": "tutorial_entrance", "east": "glyph_wall"},
                "items": []
            },
            "glyph_wall": {
                "description": "A massive wall covered in ancient glyphs blocks your way. One glyph faintly pulses.",
                "exits": {"west": "shattered_path"},
                "items": ["fragmented glyph shard"]
            }
        }

    def load_zone(self, key):
        return self.zones.get(key, {"description": "Void. Nothing exists here."})

// data/zones/zone_map.json
{
  "tutorial_entrance": {
    "description": "You awaken in a broken crypt. Echoes follow your every move.",
    "exits": {
      "north": "shattered_path"
    },
    "items": ["forgotten relic"]
  },
  "shattered_path": {
    "description": "Bones and glass litter the path. Something watches from the mist.",
    "exits": {
      "south": "tutorial_entrance",
      "east": "glyph_wall"
    },
    "items": []
  }
}


# factions/faction_system.py

class Faction:
    def __init__(self, name):
        self.name = name
        self.reputation = 0
        self.rank = "Neutral"

    def gain_reputation(self, amount):
        self.reputation += amount
        self.update_rank()

    def update_rank(self):
        if self.reputation >= 200:
            self.rank = "Ascendant"
        elif self.reputation >= 150:
            self.rank = "Bound"
        elif self.reputation >= 100:
            self.rank = "Trusted"
        elif self.reputation >= 50:
            self.rank = "Known"
        else:
            self.rank = "Neutral"

    def show_status(self):
        return f"{self.name} Rep: {self.reputation} ({self.rank})"



