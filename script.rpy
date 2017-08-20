# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
default beach = False

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    "Hello, world."

    call prologue

    menu:
        "Where would you like to go?"

        "To the beach":
            $beach = True
            e "You went to the beach. It's hot."

        "To the mountains":
            e "You went to the mountains. It's pleasantly cool."

        "Inside":
            e "You went home...."
            jump home

    e "You enjoyed yourself immensely."

    menu:
        "What was your favorite thing you did?"

        "Swimming" if beach:
            e "You had a nice long swim in the ocean."

        "Walking":
            e "You took a relaxing walk."

        "Talking with friends":
            e "You had a good time hanging out with your friends."


label home:
    e "As soon as you got home, you immediately went to sleep."
    if beach:
        e "You still have sand in your shoes."
    # This ends the game.

    return
