from bakery import assert_equal
from monster_mash import Potion, Ingredient, party1, party2, party3, party4

def get_rarest_potion(potions: list[Potion]) -> str:
    if not potions:
        return "N/A"
    
    rare_potions = []
    
    
    for potion in potions:
        for ingredient in potion.ingredients:
            if ingredient.is_rare:
                rare_potions.append(potion)
                break
    
    if not rare_potions:
        return "N/A"
    
    max_rare = 1
    rarest_potion = rare_potions[0].label   
    for rare_potion in rare_potions:
        if rare_ingredient_counter(rare_potion) > max_rare:
            rarest_potion = rare_potion.label
        
    return rarest_potion    


def rare_ingredient_counter(potion: Potion) -> int:
    #Iterates through the ingredients list of the potion to count how many rare ingredients there are
    rare_count = 0
    for ingredient in potion.ingredients:
        if ingredient.is_rare:
            rare_count += 1
    return rare_count


assert_equal(get_rarest_potion(party1.brews), "N/A")
assert_equal(get_rarest_potion(party2.brews), "Lycansoup")
assert_equal(get_rarest_potion(party3.brews), "Pumpkin Spice Latte")
assert_equal(get_rarest_potion(party4.brews), "N/A")