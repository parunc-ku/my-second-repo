
import random

class Character:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def attack(self, other):
        damage = random.uniform(
            self.attack_power * 0.3,
            self.attack_power * 0.9
        )
        damage = round(damage)
        other.hp -= damage

        print(f"{self.name} attacks {other.name} for {damage} damage!")

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return f"{self.name}: {self.hp} HP"
