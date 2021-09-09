# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define bs = Character("Big Schlong")

transform eject:
    zoom 0.1
    parallel:
        xalign 0 yalign 0.8
        linear 10.0 xalign 1 yalign 0.2 // this dont work :(
    parallel:
        linear 10.0 rotate 360



# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg space


    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    "" ""
    "" "..."

    show schlong cry at eject

    bs "yo."

    # This ends the game.S

    return
