import random

class Character:
    def __init__(self, name, image, range, base_atk, base_def, max_atk, max_def, acc, eva):
        self.name = name
        self.image = image
        self.range = range
        self.base_atk = base_atk
        self.base_def = base_def
        self.max_atk = max_atk
        self.max_def = max_def
        self.acc = acc
        self.eva = eva
        self.health = self.calculate_health()  

    def effective_attack(self):
        # Return a random value between base_atk and max_atk
        return random.uniform(self.base_atk, self.max_atk)

    def effective_defense(self):
        # Return a random value between base_def and max_def
        return random.uniform(self.base_def, self.max_def)

    def attack_hits(self, opponent):
        # Calculate hit chance based on accuracy and opponent's evasion with some randomness
        hit_chance = self.acc - opponent.eva + random.uniform(-10, 10)
        return random.uniform(0, 100) < hit_chance

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def calculate_speed(self):
        return 0.5 * self.acc + 0.5 * self.eva

    def calculate_health(self):
        alpha = 1.0
        beta = 0.5
        gamma = 0.2

        base_health = (alpha * (self.base_def + self.max_def) +
                       beta * (self.base_atk + self.max_atk) +
                       gamma * (self.acc + self.eva))

        if self.range == 's':
            return base_health * 1.2  
        elif self.range == 'm':
            return base_health * 1.1 
        elif self.range == 'l':
            return base_health * 1.0  
        else:
            return base_health  
