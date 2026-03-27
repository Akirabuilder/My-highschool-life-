# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define o = Character("Other Eileen")



###Cursor code
define config.mouse = {"default":[ ("gui/cursor.png", 1, 1) ] }


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

    e "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam et nunc nulla. Aliquam ut dui leo. Praesent elementum faucibus diam non venenatis."

    "Sed ultrices mi eget nunc mollis, quis laoreet enim lacinia. Etiam rutrum pulvinar est, ac faucibus dolor luctus id. Sed convallis eros arcu, eu iaculis turpis pharetra non. Donec viverra lectus nec risus maximus hendrerit. Aenean efficitur at libero non bibendum. Fusce convallis tempus enim, at sodales enim faucibus nec."

    e "Nullam imperdiet sapien a magna dignissim aliquet. Vivamus dictum neque non pretium tempor. Fusce quis nibh velit. Sed congue sapien id malesuada convallis."

    o "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam et nunc nulla. Aliquam ut dui leo. Praesent elementum faucibus diam non venenatis."

    $ renpy.notify("This is a notification")

    label choices:
        menu:
            "This is a sample choice menu"
            "Choice 1":
                pass
            "Choice 2":
                pass
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam et nunc nulla.":
                pass
            "Unlock some gallery images":
                show cg_3
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam et nunc nulla. Aliquam ut dui leo. Praesent elementum faucibus diam non venenatis."
                hide cg_3
                jump choices
                

    # This ends the game.

    return
