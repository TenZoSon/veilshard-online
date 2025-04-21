# combat/boss_registry.py

class Boss:
    def __init__(self, name, description, health, phases, defeat_condition, lore_fragment):
        self.name = name
        self.description = description
        self.health = health
        self.phases = phases
        self.current_phase = 0
        self.defeat_condition = defeat_condition
        self.lore_fragment = lore_fragment

    def get_phase(self):
        return self.phases[self.current_phase]

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0 and self.current_phase + 1 < len(self.phases):
            self.current_phase += 1
            self.health = self.get_phase()['health']
            return f"{self.name} shifts into a new phase!"
        elif self.health <= 0:
            return f"{self.name} has been defeated!"
        return f"{self.name} takes {amount} damage. Remaining: {self.health}"

# Sample tutorial boss
bosses = {
    "Ash-Golem Irhakor": Boss(
        name="Ash-Golem Irhakor",
        description="Forged from the smoldering remains of lost cities, Irhakor’s chest glows with ancient flame.",
        health=200,
        phases=[
            {"name": "Molten Form", "health": 200, "abilities": ["Lava Burst", "Magma Slam"]},
            {"name": "Charred Core", "health": 300, "abilities": ["Flame Cyclone", "Burning Roar"]},
        ],
        defeat_condition="Deal fire damage to weaken its armor before physical hits are effective.",
        lore_fragment="Irhakor was once a city guardian... now corrupted by unquenched fire spirits."
    )
}

# systems/taming/taming_engine.py

class TamingContract:
    def __init__(self, creature_name, required_condition, taming_difficulty):
        self.creature_name = creature_name
        self.required_condition = required_condition
        self.taming_difficulty = taming_difficulty

    def attempt_tame(self, player_level, weakened=False):
        base_chance = 0.1 + (0.05 * player_level)
        if weakened:
            base_chance += 0.25
        return base_chance >= self.taming_difficulty

# Example taming contract
contracts = {
    "Ash-Golem Irhakor": TamingContract(
        creature_name="Ash-Golem Irhakor",
        required_condition="Boss must be weakened and fought solo.",
        taming_difficulty=0.65
    )
}


# combat/skills/skill_system.py

def __init__(self, base_name, power, crit_chance, element=None, properties=None):
        self.base_name = base_name
        self.power = power
        self.crit_chance = crit_chance
        self.element = element
        self.properties = properties or []

 def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients
        power = sum(skill.power for skill in ingredients)
        crit_chance = sum(skill.crit_chance for skill in ingredients) / len(ingredients)
        element = self.determine_element(ingredients)
        properties = self.determine_properties(name)
        super().__init__(name, power, crit_chance, element, properties)

    def determine_element(self, skills):
        elems = [s.element for s in skills if s.element]
        return elems[0] if elems else None

    def determine_properties(self, name):
        props = []
        lower = name.lower()
        if "lethal" in lower:
            props += ["High Crit", "Ignores Armor"]
        if "destruction" in lower:
            props += ["Break Equipment", "Massive Power"]
        if "phantom" in lower:
            props += ["Ethereal", "Cannot Be Blocked"]
        return props

# Example base skills
base_skills = {
    "Strike": Skill("Strike", power=10, crit_chance=5),
    "Slash": Skill("Slash", power=15, crit_chance=10),
    "Burn": Skill("Burn", power=12, crit_chance=4, element="Fire"),
}

# systems/player_interaction/arena_pvp.py

class PvPChallenge:
    def __init__(self, challenger, opponent, stake_item=None, agreed=True):
        self.challenger = challenger
        self.opponent = opponent
        self.stake_item = stake_item
        self.agreed = agreed  # If false, item is dropped by loser

    def start_battle(self):
        if not self.agreed and not self.stake_item:
            return f"{self.opponent} must auto-drop a random item on loss!"
        elif self.stake_item:
            return f"{self.challenger} and {self.opponent} fight for: {self.stake_item}"
        return f"{self.challenger} vs {self.opponent}. No item stakes

