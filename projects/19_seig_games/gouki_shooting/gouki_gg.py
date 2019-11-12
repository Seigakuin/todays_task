"""Spaceship Shooter Game 10 - 左右キーでShipを動かす
"""
import random
import arcade

SPRITE_SCALING_SHIP = 0.6
SPRITE_SCALING_ENEMY = 1.0
SPRITE_SCALING_LASER = 1.0
ENEMY_COUNT = 10

GAME_STATE = 0
TIME_COUNT = 0

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600


BULLET_SPEED = 5

# Bulletを格納するリスト
BULLET_LIST = arcade.SpriteList()

# Enemy を格納するリスト
ENEMY_LIST = arcade.SpriteList()


class Ship(arcade.Sprite):
    def __init__(self):
        super().__init__("player.png", SPRITE_SCALING_SHIP)

        self.acceleration_x = 0.0
        self.change_x = 0.0

        self.moving_right = False
        self.moving_left = False

    def update(self):
        global TIME_COUNT
        self.center_x += self.change_x

        # 端っこ対策
        if self.center_y < 0:
            self.center_y = SCREEN_HEIGHT
        if self.center_y > SCREEN_HEIGHT:
            self.center_y = 0
        if self.center_x < 0:
            self.center_x = SCREEN_WIDTH
        if self.center_x > SCREEN_WIDTH:
            self.center_x = 0

        if self.moving_right:
            self.center_x += 5
        elif self.moving_left:
            self.center_x -= 5
        TIME_COUNT += 1


class Enemy(arcade.Sprite):
    def __init__(self):
        super().__init__("meteorBrown_med1.png", SPRITE_SCALING_ENEMY)
        self.change_y = random.randrange(-5, -1)
        self.center_x = random.randrange(SCREEN_WIDTH)
        self.bottom = random.randrange(500) + SCREEN_HEIGHT

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        # 端っこ対策
        if self.center_y < 0:
            self.center_y = SCREEN_HEIGHT
        if self.center_y > SCREEN_HEIGHT + 500:
            self.center_y = 0
        if self.center_x < 0:
            self.center_x = SCREEN_WIDTH
        if self.center_x > SCREEN_WIDTH:
            self.center_x = 0


class Bullet(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__("bullet.png", SPRITE_SCALING_LASER)

        self.center_x = x
        self.center_y = y

    def update(self):
        self.change_y = BULLET_SPEED
        self.center_y += self.change_y

        if self.bottom > SCREEN_HEIGHT:
            self.kill()


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Shooter")

        # Variables that will hold sprite lists
        self.ship_list = None

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

        # Set up the ship
        self.score = 0

        # Image from kenney.nl
        self.ship_sprite = Ship()
        self.ship_sprite.center_x = 50
        self.ship_sprite.center_y = 70
        self.ship_list.append(self.ship_sprite)

        # Enemyが画面に残っていたらリセット時に全て消す
        while ENEMY_LIST:
            ENEMY_LIST.pop()

        # Bulletが画面に残っていたらリセット時に全て消す
        while BULLET_LIST:
            BULLET_LIST.pop()

        # Create the enemys
        for i in range(ENEMY_COUNT):
            # Create the enemy instance
            enemy = Enemy()

            # Add the enemy to the lists
            ENEMY_LIST.append(enemy)

        # 背景用に使用する画像をロードする
        self.background = arcade.load_texture("background.png")

    def on_draw(self):
        """Render the screen.
       """
        global GAME_STATE

        # This command has to happen before we start drawing
        arcade.start_render()

        if GAME_STATE == 1:
            arcade.draw_text(
                "GAME OVER",
                SCREEN_WIDTH // 2 - 300,
                SCREEN_HEIGHT // 2,
                arcade.color.ALICE_BLUE,
                80,
            )
        elif GAME_STATE == 0:
            # ロードした背景画像を描く
            arcade.draw_texture_rectangle(
                SCREEN_WIDTH // 2,
                SCREEN_HEIGHT // 2,
                SCREEN_WIDTH,
                SCREEN_HEIGHT,
                self.background,
            )

            # Draw all the sprites.
            ENEMY_LIST.draw()

            self.ship_list.draw()
            BULLET_LIST.draw()

            # Render the text
            x = self.score
            y = TIME_COUNT % 1000

            arcade.draw_text(x + y, 800, 500, arcade.color.WHITE, 14)

    def on_key_press(self, symbol, modifiers):
        global GAME_STATE
        if GAME_STATE == 0:
            if symbol == arcade.key.SPACE:
                bullet = Bullet(
                    self.ship_sprite.center_x, self.ship_sprite.center_y
                )
                BULLET_LIST.append(bullet)

            elif symbol == arcade.key.RIGHT:
                self.ship_sprite.moving_right = True
            elif symbol == arcade.key.LEFT:
                self.ship_sprite.moving_left = True
        elif GAME_STATE == 1:
            if symbol == arcade.key.SPACE:
                self.draw_game_over()
                self.setup()
                GAME_STATE = 0

    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.RIGHT:
            self.ship_sprite.moving_right = False
        elif symbol == arcade.key.LEFT:
            self.ship_sprite.moving_left = False

    def update(self, delta_time):
        """ Movement and game logic """
        global GAME_STATE

        if GAME_STATE == 1:
            self.draw_game_over()

        elif GAME_STATE == 0:
            # Call update on all sprites
            ENEMY_LIST.update()
            BULLET_LIST.update()
            self.ship_list.update()

            ship_hit = arcade.check_for_collision_with_list(
                self.ship_sprite, ENEMY_LIST
            )

            # Game over
            if len(ship_hit) > 0:
                self.ship_sprite.kill()
                GAME_STATE = 1
                self.draw_game_over()

            # loop through each bullet
            for bullet in BULLET_LIST:

                # Check this bullet to see if it hit a enemy
                hit_list = arcade.check_for_collision_with_list(
                    bullet, ENEMY_LIST
                )

                # If it did, get rid of the bullet
                if len(hit_list) > 0:
                    bullet.kill()
                    enemy = Enemy()
                    ENEMY_LIST.append(enemy)
                for enemy in hit_list:
                    enemy.kill()

                # if GAME_STATE == 1:
                #     self.setup()

    def draw_game_over(self):
        """
        Draw "Game over" across the screen.
        """
        output = "Game Over"
        arcade.draw_text(output, 240, 400, arcade.color.WHITE, 54)

        output = "Click to restart"
        arcade.draw_text(output, 310, 300, arcade.color.WHITE, 24)


def main():
    while GAME_STATE == 0:
        window = MyGame()
        window.setup()
        arcade.run()


if __name__ == "__main__":
    main()

