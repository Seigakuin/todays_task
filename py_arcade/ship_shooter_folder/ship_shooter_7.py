"""Spaceship Shooter Game 7

Goal:
- bulletを発射するのをスペースキーにする (line 127)
- on_key_press()



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


class Ship(arcade.Sprite):
    def __init__(self):
        super().__init__("./ship.png", SPRITE_SCALING_SHIP)
        self.acceleration_x = 1.01
        self.change_x = 10

        self.moving_right = False
        self.moving_left = False

    # def apply_force(self, force)０
    #     self.acceleration_x += force

    def update(self):

        # self.change_x *= self.acceleration_x
        # self.acceleration_x *= 0.98

        if self.moving_right:
            self.center_x += self.change_x
        elif self.moving_left:
            self.center_x -= self.change_x

        self.center_y += self.change_y

        # 端っこ対策
        if self.center_y < 0:
            self.center_y = SCREEN_HEIGHT
        if self.center_y > SCREEN_HEIGHT:
            self.center_y = 0
        if self.center_x < 0:
            self.center_x = SCREEN_WIDTH
        if self.center_x > SCREEN_WIDTH:
            self.center_x = 0

        # super().update()

    def move_up(self):
        self.change_y += 5

    def move_down(self):
        self.change_y -= 5

    def move_right(self):
        self.change_x += 5
        # self.apply_force(0.2)

    def move_left(self):
        self.change_x -= 5
        # self.apply_force(-0.2)


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Shooter")

        # Variables that will hold sprite lists
        self.ship_list = None
        self.enemy_list = None
        self.bullet_list = None

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
        self.bullet_list = arcade.SpriteList()

        # Set up the ship
        self.score = 0

        # Image from kenney.nl
        self.ship_sprite = arcade.Sprite("./ship.png", SPRITE_SCALING_SHIP)
        self.ship_sprite2 = Ship()
        self.ship_sprite.center_x = 50
        self.ship_sprite.center_y = 70
        self.ship_sprite2.center_x = 150
        self.ship_sprite2.center_y = 40
        self.ship_list.append(self.ship_sprite)
        self.ship_list.append(self.ship_sprite2)

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
        self.bullet_list.draw()

        # Render the text
        arcade.draw_text(
            f"Score: {self.score}", 10, 20, arcade.color.WHITE, 14
        )

    def on_mouse_motion(self, x, y, dx, dy):
        """
        Called whenever the mouse moves.
        """
        self.ship_sprite.center_x = x
        # self.ship_sprite.center_y = y

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called whenever the mouse button is clicked.
        """
        bullet = arcade.Sprite("./laser.png", SPRITE_SCALING_LASER)

        bullet.center_x = self.ship_sprite.center_x
        bullet.center_y = self.ship_sprite.center_y + 30
        bullet.change_y = BULLET_SPEED

        # add bullet to list
        self.bullet_list.append(bullet)

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.SPACE:
            bullet = arcade.Sprite("./laser.png", SPRITE_SCALING_LASER)

            bullet.center_x = self.ship_sprite.center_x
            bullet.center_y = self.ship_sprite.center_y + 30
            bullet.change_y = BULLET_SPEED

            # add bullet to list
            self.bullet_list.append(bullet)

        if symbol == arcade.key.RIGHT:
            self.ship_sprite2.moving_right = True
        elif symbol == arcade.key.LEFT:
            self.ship_sprite2.moving_left = True

    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.RIGHT:
            self.ship_sprite2.moving_right = False
        elif symbol == arcade.key.LEFT:
            self.ship_sprite2.moving_left = False

    def update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites
        self.enemy_list.update()
        self.bullet_list.update()
        self.ship_list.update()

        # loop through each bullet
        for bullet in self.bullet_list:

            # Check this bullet to see if it hit a enemy
            hit_list = arcade.check_for_collision_with_list(
                bullet, self.enemy_list
            )

            # If it did, get rid of the bullet
            if len(hit_list) > 0:
                bullet.kill()

            # For every enemy we hit, add to the score and remove the enemy
            for enemy in hit_list:
                enemy.kill()
                self.score += 1

            # If the bullet flies off-screen, remove it.
            if bullet.bottom > SCREEN_HEIGHT:
                bullet.kill()


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
