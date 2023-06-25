import random
import math

for round in range(5):
    print("Текущий раунд -", round)
    divine_light = random.randint(1,10)
    sacred_power = random.randint(1,10)
    healing_power = 50
    character_strength = 50
    healing_multiplier_one = 1.15
    healing_multiplier_two = 1.30
    healing_power_growth = random.uniform(healing_multiplier_one, 
                                          healing_multiplier_two)
    character_strength_growth = 1.15
    blessed = divine_light + sacred_power >= 10
    if blessed:
        healing_power *= healing_power_growth
        character_strength *= character_strength_growth
        print(f"""Вы благославлены. 
Теперь ваша сила {math.ceil(character_strength)}, 
а сила лечения {math.ceil(healing_power)}\n""")
    else:
        print("Благословения нет\n")