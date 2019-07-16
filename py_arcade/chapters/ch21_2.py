"""Spaceship Shooter Game 2

Goal:
- Ship を画面下に固定、横移動のみを許す

Hint:
- on_mouse_motion()の中のコードを変更する

"""
import random
import arcade

SPRITE_SCALING_SHIP = 0.6
SPRITE_SCALING_ENEMY = 0.4
SPRITE_SCALING_LASER = 0.8
ENEMY_COUNT = 50

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

BULLET_SPEED = 5


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Shooter")

        # Variables that will hold sprite lists
        self.ship_list = None
        self.enemy_list = None

        # Set up the ship info
        self.ship_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        self.background = None

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.ship_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()

        # Set up the ship
        self.score = 0

        # Image from kenney.nl
        self.ship_sprite = arcade.Sprite("./ship.png", SPRITE_SCALING_SHIP)
        self.ship_sprite.center_x = 50
        self.ship_sprite.center_y = 70
        self.ship_list.append(self.ship_sprite)

        # Create the enemys
        for i in range(ENEMY_COUNT):

            # Create the enemy instance
            # Coin image from kenney.nl
            enemy = arcade.Sprite("./enemy.png", SPRITE_SCALING_ENEMY)

            # Position the enemy
            enemy.center_x = random.randrange(SCREEN_WIDTH)
            enemy.center_y = random.randrange(200, SCREEN_HEIGHT)

            # Add the enemy to the lists
            self.enemy_list.append(enemy)

        # 背景用に使用する画像をロードする
        self.background = arcade.load_texture("./background.png")

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # ロードした背景画像を描く
        arcade.draw_texture_rectangle(
            SCREEN_WIDTH // 2,
            SCREEN_HEIGHT // 2,
            SCREEN_WIDTH,
            SCREEN_HEIGHT,
            self.background,
        )

        # Draw all the sprites.
        self.enemy_list.draw()
        self.ship_list.draw()

        # Render the text
        arcade.draw_text(
            f"Score: {self.score}", 10, 20, arcade.color.WHITE, 14
        )

    def on_mouse_motion(self, x, y, dx, dy):
        """
        Called whenever the mouse moves.
        """
        self.ship_sprite.center_x = x
        self.ship_sprite.center_y = y

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called whenever the mouse button is clicked.
        """
        pass

    def update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites
        self.enemy_list.update()


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
