from character import Character
import random

def battle(character1, character2):
    speed1 = character1.calculate_speed()
    speed2 = character2.calculate_speed()

    if speed1 > speed2:
        first, second = character1, character2
    elif speed2 > speed1:
        first, second = character2, character1
    else:
        first, second = (character1, character2) if random.choice([True, False]) else (character2, character1)

    turn = 0
    while character1.health > 0 and character2.health > 0:
        attacker = first if turn % 2 == 0 else second
        defender = second if turn % 2 == 0 else first

        if attacker.attack_hits(defender):
            damage = max(0, attacker.effective_attack() - defender.effective_defense())
            defender.take_damage(damage)
            print(f"{attacker.name} hits {defender.name} for {damage:.2f} damage. {defender.name}'s health is now {defender.health:.2f}.")
        else:
            print(f"{attacker.name} misses {defender.name}.")

        turn += 1

    if character1.health > 0:
        print(f"{character1.name} wins!")
        return character1
    else:
        print(f"{character2.name} wins!")
        return character2

# Example characters with range
char1 = Character(name="Luke Skywalker", image="luke.jpg", range="s", base_atk=6250, base_def=6300, max_atk=8550, max_def=8650, acc=170, eva=80)
char2 = Character(name="Darth Vader", image="vader.jpg", range="s", base_atk=6590, base_def=6900, max_atk=9090, max_def=9000, acc=170, eva=80)

# Simulate battle
winner = battle(char1, char2)
