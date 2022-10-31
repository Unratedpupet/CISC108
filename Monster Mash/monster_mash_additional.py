from bakery import assert_equal
from monster_mash import Monster, Potion, Media, Ingredient, party1, party2, party3, party4


'''
# Define a function spookiest_undead that consumes a List of Monster and produces the name of the Monster that is_undead and has the highest spookiness.
def spookiest_undead(monsters: list[Monster]) -> str:
    if not monsters:
        return "N/A"
    
    monsters = is_monster_undead(monsters)
    
    if not monsters:
        return "N/A"
    
    max_spooky_value = 0
    spookiest_undead = monsters[0].name
    for monster in monsters:
        if monster.spookiness > max_spooky_value:
            max_spooky_value = monster.spookiness
            spookiest_undead = monster.name
    return spookiest_undead

def is_monster_undead(monsters: list[Monster]) -> list[Monster]:
    undead_monsters = []
    for monster in monsters:
        if monster.is_undead:
            undead_monsters.append(monster)
    return undead_monsters


assert_equal(spookiest_undead(party1.monsters), "N/A")
assert_equal(spookiest_undead(party2.monsters), "N/A")
assert_equal(spookiest_undead(party3.monsters), "Winnie Sanderson")
assert_equal(spookiest_undead(party4.monsters), "Jack Skellington")
'''

'''
# Define a function turn_undead that consumes a List of Monster and produces a new list of Monster where all the is_undead fields are set to False and the spookiness is set to 1.
def turn_undead(monsters: list[Monster]) -> list[Monster]:
    if not monsters:
        return monsters
    
    for monster in monsters:
        if monster.is_undead:
            monster.spookiness = 1
            monster.is_undead = False
    return monsters

# Test cases with better formating
monsters1 = []
monsters2 = [
        Monster("Tracy Pawdan", "werewolf", 2, False),
        Monster("Liz Lemoon", "werewolf", 1, False),
        Monster("Bark Donaghy", "werewolf", 2, False)
        ]
monsters3 = [
        Monster("Winnie Sanderson", "witch", 1, False),
        Monster("Zachary Binx", "cat", 0, False),
        Monster("Wanda Maximoff", "witch", 3, False),
        Monster("Sabrina Spellman", "witch", 1, False),
        Monster("Hermione Granger", "witch", 0, False),
    ]
monsters4 = [
        Monster("Jack Skellington", "skeleton", 1, False),
        Monster("Sally", "doll", 0, False),
        Monster("Oogie Boogie", "bug bag", 3, False),
        Monster("Zero", "ghost", 1, False),
        Monster("The Mayor", "politician", 3, False),
        Monster("Werewolf", "werewolf", 1, False)
    ]


assert_equal(turn_undead(party1.monsters), monsters1)
assert_equal(turn_undead(party2.monsters), monsters2)
assert_equal(turn_undead(party3.monsters), monsters3)
assert_equal(turn_undead(party4.monsters), monsters4)
'''

'''
# Define a function total_songs that consumes a list of Media and produces the sum of the duration of the "song" kind.
def total_songs(medias: list[Media]) -> int:
    if not medias:
        return 0
    
    total_duration = 0
    for song in medias:
        if song.kind == "song":
            total_duration += song.duration
    return total_duration

assert_equal(total_songs(party1.media), 0)
assert_equal(total_songs(party2.media), 3)
assert_equal(total_songs(party3.media), 7)
assert_equal(total_songs(party4.media), 15)
'''

'''
# Define a function average_duration that consumes a list of Media and produces the average duration of all Media.
def average_duration(medias: list[Media]) -> float:
    if not medias:
        return 0
    
    total_time = 0
    number_of_media = 0
    for media in medias:
        number_of_media += 1
        total_time += media.duration
    return total_time / number_of_media

assert_equal(average_duration(party1.media), 0)
assert_equal(average_duration(party2.media), (3+92+10)/3)
assert_equal(average_duration(party3.media), (96+2+5+350)/4)
assert_equal(average_duration(party4.media), (3+3+2+4+3)/5)
'''

'''
# Define a function list_options that consumes a list of Potion and produces a single string that joins together the label of each of the potions with commas
def list_options(potions: list[Potion]) -> str:
    if not potions:
        return "No potions"
    
    potion_labels = ""
    for potion in potions:
        potion_labels += potion.label + ","
        #Strips the last character, removing the last comma.
    return potion_labels[:-1]

assert_equal(list_options(party1.brews), "No potions")
assert_equal(list_options(party2.brews), "Hair o' the Dog,Lycansoup,Howler")
assert_equal(list_options(party3.brews), "Witches Brew,Sleeping Draught,Pumpkin Spice Latte")
assert_equal(list_options(party4.brews), "Foggy Night,Delicious Soup")
'''


#Define a function total_rare_brew_time that consumes a list of Potion and produces the sum of all the time_required to brew
#each Potion, but only if the Potion has an ingredient that is_rare.
