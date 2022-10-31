"""
🎃 Monster Mash 🎃
"""
from dataclasses import dataclass
from bakery import assert_equal


@dataclass
class Party:
    """
    Metadata about the party including its name, venue, and size.

    Attributes:
        theme: A descriptive name for the party
        venue: The name of the location where the party was hosted
        capacity: How many monsters the venue can fit
        head_count: The number of monsters that actually showed up
    """

    theme: str
    venue: str
    capacity: int
    head_count: int


@dataclass
class Monster:
    """
    A representation of a specific monster attending the party.

    Attributes:
        name: The name of this particular monster
        kind: The type of this monster (e.g., "vampire", "werewolf")
        spookiness: An integer from 0-4 indicating how scary the monster is
        is_undead: Whether or not this monster is undead or not (e.g., a zombie, vampire)
    """

    name: str
    kind: str
    spookiness: int
    is_undead: bool


@dataclass
class Media:
    """
    Either a song, movie, or game that is played at the party.

    Attributes:
        name: The name of this piece of media
        kind: Either "movie", "song", or "game"
        duration: The length of this media in minutes
    """

    name: str
    kind: str
    duration: int


@dataclass
class Ingredient:
    """
    A specific ingredient for a potion. May or may not be rare.

    Attributes:
        name: The name of this ingredient
        is_rare: Whether or not the ingredient is rare
    """

    name: str
    is_rare: bool


@dataclass
class Potion:
    """
    A (possibly delicious) magical potion that can be consumed to
    produce a certain magical effect. Requires ingredients and time
    to brew.

    Attributes:
        label: The name of the potion, according to its label
        time_required: How many minutes are required to brew the potion
        ingredients: A list of the ingredients required
    """

    label: str
    time_required: int
    ingredients: list[Ingredient]


@dataclass
class MonsterMash:
    """
    All of the data related to a single instance of a monster party, including
    some of the key monsters attending, what media they enjoyed, and the drinks
    they had (brews).

    Attributes:
        party: The metadata about the party
        monsters: A list of the coolest monsters in attendance
        media: A list of the best songs, games, and movies they enjoyed
        brews: The potions that they served as beverages
    """

    party: Party
    monsters: list[Monster]
    media: list[Media]
    brews: list[Potion]


################### Data ###################

party1 = MonsterMash(Party("Ghostly Gala", "Nearby Graveyard", 10, 0), [], [], [])

party2 = MonsterMash(
    Party("Werewolf Bar Mitzvah", "30 Rockefeller Plaza", 5, 3),
    [
        Monster("Tracy Pawdan", "werewolf", 2, False),
        Monster("Liz Lemoon", "werewolf", 1, False),
        Monster("Bark Donaghy", "werewolf", 2, False),
    ],
    [
        Media("Werewolves of London", "song", 3),
        Media("Teen Wolf", "movie", 92),
        Media("Fetch", "game", 10),
    ],
    [
        Potion(
            "Hair o' the Dog",
            4,
            [Ingredient("Suspicious fur", False), Ingredient("Moon Blooms", True)],
        ),
        Potion(
            "Lycansoup",
            8,
            [
                Ingredient("Bone", False),
                Ingredient("Scooby Snacks", True),
                Ingredient("Moon Blooms", True),
            ],
        ),
        Potion(
            "Howler",
            5,
            [
                Ingredient("Wheat", False),
                Ingredient("Yeast", False),
                Ingredient("Moon Blooms", True),
            ],
        ),
    ],
)

party3 = MonsterMash(
    Party("Witches Ball", "Salem Dance Hall", 100, 35),
    [
        Monster("Winnie Sanderson", "witch", 3, True),
        Monster("Zachary Binx", "cat", 0, False),
        Monster("Wanda Maximoff", "witch", 3, False),
        Monster("Sabrina Spellman", "witch", 1, False),
        Monster("Hermione Granger", "witch", 0, False),
    ],
    [
        Media("Hocus Pocus", "movie", 96),
        Media("I Put a Spell on You", "song", 2),
        Media("Hedwig's Theme", "song", 5),
        Media("Wandavision", "movie", 350),
    ],
    [
        Potion(
            "Witches Brew",
            56,
            [
                Ingredient("Toe of Frog", False),
                Ingredient("Wool of Bat", False),
                Ingredient("Adders Fork", False),
            ],
        ),
        Potion(
            "Sleeping Draught",
            29,
            [Ingredient("Benedryll", False), Ingredient("Nyqil", False)],
        ),
        Potion(
            "Pumpkin Spice Latte",
            5,
            [
                Ingredient("Milk", False),
                Ingredient("Pumpkin", False),
                Ingredient("Spices", True),
                Ingredient("Coffee Beans", False),
            ],
        ),
    ],
)

party4 = MonsterMash(
    Party("Halloween Town Festival", "Halloween Town", 300, 230),
    [
        Monster("Jack Skellington", "skeleton", 2, True),
        Monster("Sally", "doll", 0, False),
        Monster("Oogie Boogie", "bug bag", 3, False),
        Monster("Zero", "ghost", 1, True),
        Monster("The Mayor", "politician", 3, False),
        Monster("Werewolf", "werewolf", 1, False)
    ],
    [
        Media("This is Halloween", "song", 3),
        Media("What's This?", "song", 3),
        Media("Sally's Song", "song", 2),
        Media("Making Christmas", "song", 4),
        Media("Oogie Boogie's Song", "song", 3),
    ],
    [
        Potion("Foggy Night", 3, [Ingredient("Fog Juice", False)]),
        Potion(
            "Delicious Soup",
            5,
            [
                Ingredient("Soup", False),
                Ingredient("Worm's Wort", False),
                Ingredient("Deadly Night Shade", False),
            ],
        ),
    ],
)

