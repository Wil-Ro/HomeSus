# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define bs = Character("Big Schlong")
define mc = Character("[name]")


transform eject:
    zoom 0.1
    parallel:
        xalign -0.1 yalign 0.8
        linear 30.0 xalign 1.1 yalign 0.2
    parallel:
        linear 30.0 rotate 360



# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    image deltarune = Movie(play = "deltarune.webm", mask = "deltarune-mask.webm", channel = "deltarunenoise")

    show deltarune


    python:
        name = renpy.input("name?", default = "enter name")
        name = name.strip()
        if not name or name == "enter name":
            name = "Red"
    
    stop deltarunenoise fadeout 1.0
    hide deltarune with fade
    pause 1.0
    scene bg space with fade


    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.


    show mc normal at eject

    "" "..."
    "" "[name] has been ejected, 1 impostor remains"
    mc "..."
    mc "fuck"

    scene bg school-corridor with fade

    mc "..."
    mc ".. where am I?"

    # This ends the game.S

    return
