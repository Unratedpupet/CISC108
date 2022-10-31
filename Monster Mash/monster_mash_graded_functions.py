from bakery import assert_equal
from monster_mash import Party, Monster, Media, Potion, Ingredient, party1, party2, party3, party4

'''
Starts the lecture and practicum functions
'''
'''
Party Ratio
'''
def get_party_ratio(party: Party) -> float:
    if party.capacity == 0:
        return 0.0
    else:
        return party.head_count / party.capacity


assert_equal(get_party_ratio(party1.party), 0.0)
assert_equal(get_party_ratio(party2.party), 3/5)
assert_equal(get_party_ratio(party3.party), 35/100)
assert_equal(get_party_ratio(party4.party), 230/300)

'''
Average Spookiness
'''
def average_spookiness(monsters: list[Monster]) -> float:
    total_spookiness = 0
    monster_count = 0
    for monster in monsters:
        total_spookiness += monster.spookiness
        monster_count += 1
    if monster_count == 0:
        return  0.0
    else:
        return total_spookiness / monster_count
    




assert_equal(average_spookiness(party1.monsters), 0.0)
assert_equal(average_spookiness(party2.monsters), 5/3)
assert_equal(average_spookiness(party3.monsters), 7/5)
assert_equal(average_spookiness(party4.monsters), 10/6)

'''
Last Song
'''
def last_song(medias: list[Media]) -> str:
    song = "no songs"
    for media in medias:
        if media.kind == "song":
            if media.kind == "song":
                song = media.name
    return song


assert_equal(last_song(party1.media), "no songs")
assert_equal(last_song(party2.media), "Werewolves of London")
assert_equal(last_song(party3.media), "Hedwig's Theme")
assert_equal(last_song(party4.media), "Oogie Boogie's Song")

'''
Longest Movie
'''
def longest_movie(media: list[Media]) -> str:
    if not media:
        return "no movies"
    
    max_duration = 0
    long_movie = "no movies"
    for movie in media:
        if movie.kind == "movie":
            if movie.duration > max_duration:
                max_duration = movie.duration
                long_movie = movie.name
        
    return long_movie


assert_equal(longest_movie(party1.media), "no movies")
assert_equal(longest_movie(party2.media), "Teen Wolf")
assert_equal(longest_movie(party3.media), "Wandavision")
assert_equal(longest_movie(party4.media), "no movies")

'''
Brew Time Per Ingredient
'''
def brew_time_per_ingredient(potions: list[Potion]) -> float:
    if not potions:
        return 0.0
    
    total_brew_time = 0
    total_ingredients = 0
    
    for potion in potions:
        total_brew_time += potion.time_required
        for ingredient in potion.ingredients:
            total_ingredients += 1
            
    return total_brew_time / total_ingredients
 

assert_equal(brew_time_per_ingredient(party1.brews), 0.0)
assert_equal(brew_time_per_ingredient(party2.brews), 17/8)
assert_equal(brew_time_per_ingredient(party3.brews), (56+29+5)/9)
assert_equal(brew_time_per_ingredient(party4.brews), 2.0)


'''
Get rarest Potion
'''
def get_rarest_potion(potions: list[Potion]) -> str:
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