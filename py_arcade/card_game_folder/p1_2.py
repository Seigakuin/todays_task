import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Dice!!!"

# Create SpriteList to store die sprites
die_list = arcade.SpriteList()

# Create all die sprites
die1 = arcade.Sprite("img/dieWhite1.png")
die2 = arcade.Sprite("img/dieWhite2.png")
die3 = arcade.Sprite("img/dieWhite3.png")
die4 = arcade.Sprite("img/dieWhite4.png")
die5 = arcade.Sprite("img/dieWhite5.png")
die6 = arcade.Sprite("img/dieWhite6.png")

die_list.append(die1)
die_list.append(die2)
die_list.append(die3)
die_list.append(die4)
die_list.append(die5)
die_list.append(die6)

die1.set_position(SCREEN_WIDTH / 2 + 100, SCREEN_HEIGHT / 2)
die2.set_position(SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2)

chosen_die = die_list[0]


# def choose_die():
#     global chosen_die
#     num = random.randint(0, 5)

#     chosen_die = die_list[num]


def draw_die():
    global chosen_die
    # choose_die()

    chosen_die.draw()


def on_draw(delta_time):
    global chosen_die
    chosen_die.set_position(100, 100)
    chosen_die.draw()


def on_key_press(key, modifier):
    global chosen_die
    if key == arcade.key.UP:
        print(f"key  {key}")
        chosen_die = die_list[random.randint(0, 5)]


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.set_background_color(arcade.color.AMAZON)
    arcade.start_render()

    # # Draw a snow person
    # die1 = arcade.Sprite("img/dieWhite1.png")
    # die1.center_x = SCREEN_WIDTH / 2
    # die1.center_y = SCREEN_HEIGHT / 2

    arcade.draw_text(
        "DICE!!!!",
        SCREEN_WIDTH / 2,
        SCREEN_HEIGHT - 100,
        arcade.color.AERO_BLUE,
        44,
        align="center",
        anchor_x="center",
        anchor_y="center",
    )

    # Finish and run
    arcade.finish_render()

    arcade.schedule(on_draw, 1 / 40)
    arcade.run()


# Call the main function to get the program started.
main()

'''
class MyGame(arcade.Window):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.AMAZON)

        # If you have sprite lists, you should create them here,
        # and set them to None

    def setup(self):
        # Create your sprites and sprite lists here
        self.dice_list = arcade.SpriteList()

        dice_list = [
            arcade.Sprite("img/dieWhite1.png"),
            arcade.Sprite("img/dieWhite2.png"),
            arcade.Sprite("img/dieWhite3.png"),
            arcade.Sprite("img/dieWhite4.png"),
            arcade.Sprite("img/dieWhite5.png"),
            arcade.Sprite("img/dieWhite6.png"),
        ]
        # self.dice_sprite1 = arcade.Sprite("img/dieWhite1.png")
        # self.dice_sprite2 = arcade.Sprite("img/dieWhite2.png")
        # self.dice_sprite3 = arcade.Sprite("img/dieWhite3.png")
        # self.dice_sprite4 = arcade.Sprite("img/dieWhite4.png")
        # self.dice_sprite5 = arcade.Sprite("img/dieWhite5.png")
        # self.dice_sprite6 = arcade.Sprite("img/dieWhite6.png")

        for d in dice_list:
            self.dice_list.append(d)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()

        self.dice_list[0].center_x = SCREEN_WIDTH / 2
        self.dice_list[0].center_y = SCREEN_HEIGHT / 2

        self.dice_list[0].draw()

    def update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        pass

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        http://arcade.academy/arcade.key.html
        """
        pass

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass


def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
'''
