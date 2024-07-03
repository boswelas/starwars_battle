from character import Character
import random

def battle(character1_data, character2_data):
    print(f"in the battle function")
    character1 = Character(
        name=character1_data[1],
        image=character1_data[2],
        range=character1_data[3],
        base_atk=character1_data[4],
        base_def=character1_data[5],
        max_atk=character1_data[6],
        max_def=character1_data[7],
        acc=character1_data[8],
        eva=character1_data[9]
    )
    print(f"made Character 1: ", character1.name)
    character2 = Character(
        name=character2_data[1],
        image=character2_data[2],
        range=character2_data[3],
        base_atk=character2_data[4],
        base_def=character2_data[5],
        max_atk=character2_data[6],
        max_def=character2_data[7],
        acc=character2_data[8],
        eva=character2_data[9]
    )
    print(f"made Character 2: ", character2.name)

    battle_play = []
    battle_play.append(f"Battle between {character1.name} and {character2.name}.")

    speed1 = character1.calculate_speed()
    speed2 = character2.calculate_speed()
    if speed1 > speed2:
        first, second = character1, character2
    elif speed2 > speed1:
        first, second = character2, character1
    else:
        first, second = (character1, character2) if random.choice([True, False]) else (character2, character1)

    turn = 0
    turn_limit = 20

    while character1.health > 0 and character2.health > 0:
        if turn >= turn_limit:
            # Determine which character makes the critical attack
            if character1.health > character2.health:
                attacker, defender = character1, character2
            else:
                attacker, defender = character2, character1
            damage = defender.health  # Critical attack to take out total HP
            defender.take_damage(damage)
            battle_play.append(f"{attacker.name} makes a critical attack on {defender.name} for {damage:.2f} damage. {defender.name}'s health is now 0.00.")
            break

        attacker = first if turn % 2 == 0 else second
        defender = second if turn % 2 == 0 else first

        if attacker.attack_hits(defender):
            damage = max(0, attacker.effective_attack() - defender.effective_defense())
            critical_hit = random.random() < 0.1  # 10% chance of critical hit
            if critical_hit:
                damage *= 1.5
                battle_play.append(f"Critical hit!")
            defender.take_damage(damage)
            battle_play.append(f"{attacker.name} hits {defender.name} for {damage:.2f} damage. {defender.name}'s health is now {defender.health:.2f}.")
        else:
            battle_play.append(f"{attacker.name} misses {defender.name}.")

        turn += 1

    if character1.health > 0 and character2.health <= 0:
        battle_play.append(f"{character1.name} wins!")
        battle_play.append(f"{character2.name}")
    elif character2.health > 0 and character1.health <= 0:
        battle_play.append(f"{character2.name} wins!")
        battle_play.append(f"{character1.name}")
    else:
        if character1.health > character2.health:
            battle_play.append(f"{character1.name} wins!")
            battle_play.append(f"{character2.name}")
        else:
            battle_play.append(f"{character2.name} wins!")
            battle_play.append(f"{character1.name}")

    return battle_play
