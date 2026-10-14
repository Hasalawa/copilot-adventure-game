"""A small command-line choose-your-own-adventure game."""


# Each scene is a function so that the story's branches remain easy to read.
def scene_crossroads():
    """The player chooses how to begin the adventure."""
    print("\nSCENE 1: THE CROSSROADS")
    print("A weathered sign points toward a moonlit forest, a lonely tower, and a river.")
    print("1. Follow the forest path")
    print("2. Climb the hill toward the tower")
    print("3. Walk down to the river")

    choice = get_choice(3)
    return {1: scene_forest, 2: scene_tower, 3: scene_river}[choice]


def scene_forest():
    """A forest encounter that rewards either kindness or caution."""
    print("\nSCENE 2: THE WHISPERING FOREST")
    print("The trees whisper your name. A small fox is caught in a silver snare.")
    print("1. Free the fox")
    print("2. Keep walking quietly")
    print("3. Take the silver snare")

    choice = get_choice(3)
    if choice == 1:
        print("The grateful fox trots ahead and leads you toward a hidden garden.")
        return scene_garden
    if choice == 2:
        print("The whispers grow louder until the path disappears beneath your feet.")
        return ending_lost
    print("The snare tightens around your boot. The forest keeps your prize and your freedom.")
    return ending_trapped


def scene_tower():
    """A puzzle scene at the top of the hill."""
    print("\nSCENE 2: THE CLOCKWORK TOWER")
    print("At the tower door, three symbols glow: a sun, a key, and an eye.")
    print("An inscription reads: 'I open every morning, but I am not a door.'")
    print("1. Press the sun")
    print("2. Press the key")
    print("3. Press the eye")

    choice = get_choice(3)
    if choice == 1:
        print("Warm light spills across the stones, revealing a staircase inside.")
        return scene_rooftop
    if choice == 2:
        print("The key symbol clicks. A hidden door opens beneath the tower.")
        return scene_treasure
    print("The eye opens. A stone guardian wakes and asks you to prove your courage.")
    return scene_guardian


def scene_river():
    """The river offers several risky ways to cross."""
    print("\nSCENE 2: THE STARLIT RIVER")
    print("The river is too wide to jump. A boat, a rope bridge, and stepping stones wait nearby.")
    print("1. Take the boat")
    print("2. Cross the rope bridge")
    print("3. Use the stepping stones")

    choice = get_choice(3)
    if choice == 1:
        print("The current carries the boat toward a bright island in the river's center.")
        return scene_island
    if choice == 2:
        print("The bridge sways, but you reach the far bank and find a lantern-lit road.")
        return scene_rooftop
    print("The stones shift under your feet. You swim to shore beside a locked iron gate.")
    return scene_treasure


def scene_garden():
    """A peaceful route that ends with a choice about the garden's magic."""
    print("\nSCENE 3: THE HIDDEN GARDEN")
    print("The fox brings you to a garden where a silver tree bears one glowing fruit.")
    print("1. Eat the fruit")
    print("2. Plant the fruit's seed")
    print("3. Leave the garden untouched")

    choice = get_choice(3)
    if choice == 1:
        return ending_wish
    if choice == 2:
        return scene_rooftop
    return ending_peace


def scene_rooftop():
    """The player reaches the final viewpoint and chooses what to do with the map."""
    print("\nSCENE 4: ABOVE THE CLOUDS")
    print("On the tower roof, an old map reveals every secret road in the kingdom.")
    print("1. Share the map with the villagers")
    print("2. Keep the map for yourself")
    print("3. Burn the map and return home")

    choice = get_choice(3)
    if choice == 1:
        return ending_hero
    if choice == 2:
        return ending_ruler
    return ending_peace


def scene_treasure():
    """A treasure chamber with a choice between gold and a useful relic."""
    print("\nSCENE 3: THE TREASURE CHAMBER")
    print("The gate opens into a chamber containing a crown, a healing bell, and a blank book.")
    print("1. Take the crown")
    print("2. Ring the healing bell")
    print("3. Write your own story in the book")

    choice = get_choice(3)
    if choice == 1:
        return ending_ruler
    if choice == 2:
        return ending_hero
    return scene_rooftop


def scene_guardian():
    """The guardian tests whether the player values courage over certainty."""
    print("\nSCENE 3: THE STONE GUARDIAN")
    print("The guardian asks: 'What grows stronger when it is shared?'")
    print("1. Gold")
    print("2. Knowledge")
    print("3. Silence")

    choice = get_choice(3)
    if choice == 2:
        print("The guardian smiles and steps aside, revealing the tower roof.")
        return scene_rooftop
    return ending_guardian


def scene_island():
    """A mysterious island offers a final magical decision."""
    print("\nSCENE 3: THE RIVER ISLAND")
    print("A lighthouse keeper offers you one lantern. It can guide you or light the whole river.")
    print("1. Guide your own way home")
    print("2. Light the whole river for travelers")
    print("3. Drop the lantern into the water")

    choice = get_choice(3)
    if choice == 1:
        return ending_peace
    if choice == 2:
        return ending_hero
    return ending_wish


# Ending functions return None, which tells the game loop that the story is over.
def ending_hero():
    print("\nENDING: THE OPEN-HANDED HERO")
    print("Your choice helps travelers across the kingdom. Songs are written about your generosity.")
    return None


def ending_ruler():
    print("\nENDING: THE SECRET KEEPER")
    print("You gain great power, but every secret makes the world a little lonelier.")
    return None


def ending_wish():
    print("\nENDING: THE BRIGHT WISH")
    print("The magic changes your life, and you use your new gift to grant kindness wherever you go.")
    return None


def ending_peace():
    print("\nENDING: A QUIET RETURN")
    print("You return home with no treasure, but with a story that will keep you smiling for years.")
    return None


def ending_lost():
    print("\nENDING: THE FOREST'S SECRET")
    print("You become part of the forest's whispering legend. Perhaps another traveler will find you.")
    return None


def ending_trapped():
    print("\nENDING: THE SILVER SNARE")
    print("The adventure ends early. Next time, remember that curiosity is not the same as taking.")
    return None


def ending_guardian():
    print("\nENDING: THE UNCONVINCED GUARDIAN")
    print("The guardian sends you home to think about your answer. The tower will still be waiting.")
    return None


def get_choice(number_of_choices):
    """Read a numbered choice and keep asking until the input is valid."""
    while True:
        answer = input("\nChoose an option: ").strip()
        try:
            choice = int(answer)
        except ValueError:
            print("Please enter a number.")
            continue

        if 1 <= choice <= number_of_choices:
            return choice
        print(f"Please choose a number from 1 to {number_of_choices}.")


def play_game():
    """Run one game, then offer the player the option to replay."""
    print("WELCOME TO THE MOONLIT MAP")
    print("Your choices shape the story. Choose carefully!")

    while True:
        # The current scene returns the next scene, so this loop follows the branch.
        next_scene = scene_crossroads
        while next_scene is not None:
            next_scene = next_scene()

        replay = input("\nPlay again? (y/n): ").strip().lower()
        if replay != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    play_game()
