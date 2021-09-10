# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define bigSchlong = Character("Big Schlong")
define mc = Character("[name]")
define aradia = Character("Aradia")
define wheatly = Character("Wheatly")
define glados = Character("GladOs")
define miku = Character("Hatsune Miku")

# these are animations and positions we can send the character sprites to, to use them just show the character and put "at [transform name]" at the end, e.g. "show sans at eject" would make sans be small and zoom across the screen as if ejected into space
transform eject:
    zoom 0.1
    parallel:
        xalign -0.1 yalign 0.8
        linear 30.0 xalign 1.1 yalign 0.2
    parallel:
        linear 30.0 rotate 360

transform resignation:
    linear 1.0 zoom 0.5 xalign 0.2 yalign 0.5

transform resigned:
    xalign 0.2 yalign 0.5

transform upclose:
    zoom 3.5
    xalign 0.5
    yalign 0.2


# The game starts here.

label start:
    jump ch1

label ch1:
    # set up a quirky video
    image deltarune = Movie(play = "deltarune.webm", mask = "deltarune-mask.webm", channel = "filmnoise")
    # play quirky video as a background
    show deltarune

    # run some python code to get the players name, this is now stored in a variable accessed through typing [name]
    python:
        name = renpy.input("name?", default = "enter name")
        name = name.strip()
        if not name or name == "enter name":
            name = "Red"
    
    # fade out the music and video, cut to background of space
    stop filmnoise fadeout 1.0
    hide deltarune with fade
    pause 1.0
    scene bg space with fade

    #show the main characters sprite using a nice transform defined a bit earlier on that shrinks them and makes them spin on the screen

    show mc normal at eject

    "..."
    "[name] has been ejected, 1 impostor remains"
    mc "..."
    mc "fuck"

    scene bg school-corridor with fade

    mc "..."
    mc "ow, my head"
    mc ".. where am I?"

    show aradia normal

    aradia "hey, what are you doing on the floor?"
    "a character comes up to you, half chuckling to herself as she approaches"
    aradia "you're gonna be late for class if you stay lying down there"
    "she helps you up onto your feet"
    mc "what"
    mc "wait sorry, who are you? Why am I.."
    aradia "what do you mean who am I?"
    aradia "its me? Aradia! Your childhood friend"
    mc "..."
    aradia "wow, that fall must have really taken it out of you"
    aradia "look, no matter, you'll probably recover soon, we need to get you to maths class"
    "the stranger begins to drag you down the corridor towards a nearby classroom"

    scene bg school-classroom

    "the classroom is filled with noise and a large variety of students, all fighting, shouting and playing"
    "a small robot sits at the front of the class, he's trying to calm the class down"

    show wheatly normal

    wheatly "hey! hey! Quieten down"
    "he sighs before resigning to his failiure"

    show wheatly normal at resignation
    "suddenly the room shakes and a large, robot invades the room"

    show glados normal at right
    "no"

    wheatly "*dies*"

    image explosion = Movie(play = "explosion.webm", mask = "explosion-mask.webm", channel = "filmnoise", loops = 1)

    show explosion at resigned
    hide wheatly
    pause 5.0
    hide explosion

    
    glados "now you will all learn maths"

    "you feel a tap on your shoulder"

    show miku normal at left

    "its a weird ass ugly 2d fucker thing..."
    "ew"

    hide glados
    show miku normal at upclose

    miku "hey this maths is hard, got any idea whats going on?"
    mc "2+2=4"
    miku "holy shit you're a genius"

    # This ends the game.

    return
