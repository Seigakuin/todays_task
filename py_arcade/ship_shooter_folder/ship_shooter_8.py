"""Spaceship Shooter Game 8

Added Features:
    - Added Acceleration
    - Added Start Page, Game Over Page
    - Added Shoot while pressing down
    - Added move while pressing down
    - Added classes to Enemy, Bullets
    - Made SpriteList a global variable (BULLET_LIST, ENEMY_LIST)
    - Added time module to use for timing functionalities


"""
import random
import arcade
import time

SPRITE_SCALING_SHIP = 0.6
SPRITE_SCALING_ENEMY = 0.4
SPRITE_SCALING_LASER = 1.8
ENEMY_COUNT = 30

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

BULLET_SPEED = 5

MAX_SPEED = 30

# Bulletを格納するリスト
BULLET_LIST = arcade.SpriteList()

# Enemy を格納するリスト
ENEMY_LIST = arcade.SpriteList()

# STATES
START = 0
INSTRUCTION_PAGE_1 = 1
GAME_RUNNING = 2
GAME_OVER = 3


class Ship(arcade.Sprite):
    def __init__(self):
        super().__init__("./ship.png", SPRITE_SCALING_SHIP)
        self.acceleration_x = 0.0
        self.change_x = 0.0

        self.moving_right = False
        self.moving_left = False

        self.shoot_delay = 0.05
        self.last_shot = time.perf_counter()

        self.shooting = False

    def shoot(self):
        now = time.perf_counter()

        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            bullet = Bullet(self)
            BULLET_LIST.append(bullet)

    def update(self):

        # if acc is over max_speed
        if self.change_x > MAX_SPEED:
            self.change_x = MAX_SPEED
        elif self.change_x < -MAX_SPEED:
            self.change_x = -MAX_SPEED
        else:
            self.change_x += self.acceleration_x
        self.change_x *= 0.94
        self.acceleration_x *= 0.92

        if self.moving_right:
            self.acceleration_x += 0.1
        elif self.moving_left:
            self.acceleration_x -= 0.1
        self.center_x += self.change_x

        # Bullet shoot 処理
        if self.shooting:
            self.shoot()

        # 端っこ対策
        if self.center_y < 0:
            self.center_y = SCREEN_HEIGHT
        if self.center_y > SCREEN_HEIGHT:
            self.center_y = 0
        if self.center_x < 0:
            self.center_x = SCREEN_WIDTH
        if self.center_x > SCREEN_WIDTH:
            self.center_x = 0


class Enemy(arcade.Sprite):
    def __init__(self):
        super().__init__("./enemy.png", SPRITE_SCALING_ENEMY)
        self.change_y = random.randrange(-5, -1)
        self.center_x = random.randrange(SCREEN_WIDTH)
        self.bottom = random.randrange(500) + SCREEN_HEIGHT
        # self.center_y = random.randrange(500)

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
    def __init__(self, ship):
        super().__init__("./laser.png", SPRITE_SCALING_LASER)
        self.ship = ship

        self.center_x = self.ship.center_x
        self.center_y = self.ship.center_y + 30

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

        self.shooting = False

        # self.now = time.perf_counter()
        self.last_enemy_create = time.perf_counter()
        self.enemy_create_delay = 1
        self.enemy_count = 0

        # STATES
        self.current_state = START

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.ship_list = arcade.SpriteList()

        # Set up the ship
        self.score = 0

        # Image from kenney.nl
        self.ship_sprite = Ship()
        self.ship_sprite.center_x = SCREEN_WIDTH // 2
        self.ship_sprite.center_y = 70
        self.ship_list.append(self.ship_sprite)

        while ENEMY_LIST:
            ENEMY_LIST.pop()

        while BULLET_LIST:
            BULLET_LIST.pop()

        # Create the enemys
        for i in range(ENEMY_COUNT):

            # Create the enemy instance
            enemy = Enemy()
            # Add the enemy to the lists
            ENEMY_LIST.append(enemy)

        # 背景用に使用する画像をロードする
        self.background = arcade.load_texture("./background.png")

    def draw_start_page(self):
        """
        Draw a start page
        """
        # ロードした背景画像を描く
        arcade.draw_texture_rectangle(
            SCREEN_WIDTH // 2,
            SCREEN_HEIGHT // 2,
            SCREEN_WIDTH,
            SCREEN_HEIGHT,
            self.background,
        )
        self.background = arcade.load_texture("./start.png")

        # Render the text
        arcade.draw_text(
            f"START",
            SCREEN_WIDTH // 2 - 200,
            SCREEN_HEIGHT // 2,
            arcade.color.WHITE,
            100,
        )

        arcade.draw_text(
            f"Click mouse to start...",
            SCREEN_WIDTH // 2 - 250,
            SCREEN_HEIGHT // 2 - 100,
            arcade.color.WHITE,
            40,
        )

    def draw_gameover_page(self):
        """
        Draw a gameover page
        """
        # ロードした背景画像を描く
        arcade.draw_texture_rectangle(
            SCREEN_WIDTH // 2,
            SCREEN_HEIGHT // 2,
            SCREEN_WIDTH,
            SCREEN_HEIGHT,
            self.background,
        )
        self.background = arcade.load_texture("./start.png")

        # Render the text
        arcade.draw_text(
            f"GAME OVER",
            SCREEN_WIDTH // 2 - 330,
            SCREEN_HEIGHT // 2,
            arcade.color.WHITE,
            100,
        )

        arcade.draw_text(
            f"Click mouse to continue...",
            SCREEN_WIDTH // 2 - 330,
            SCREEN_HEIGHT // 2 - 100,
            arcade.color.WHITE,
            40,
        )

    def draw_game(self):
        """
        Render the screen.
        """

        # ロードした背景画像を描く
        arcade.draw_texture_rectangle(
            SCREEN_WIDTH // 2,
            SCREEN_HEIGHT // 2,
            SCREEN_WIDTH,
            SCREEN_HEIGHT,
            self.background,
        )
        self.background = arcade.load_texture("./background.png")

        # Draw all the sprites.
        ENEMY_LIST.draw()
        self.ship_list.draw()
        BULLET_LIST.draw()
        # self.bullet_list.draw()

        # Render the text
        arcade.draw_text(
            f"Score: {self.score}", 10, 20, arcade.color.WHITE, 14
        )

    def on_draw(self):
        arcade.start_render()

        if self.current_state == START:
            self.draw_start_page()
        elif self.current_state == GAME_RUNNING:
            self.draw_game()
        elif self.current_state == GAME_OVER:
            self.draw_gameover_page()

    def on_mouse_motion(self, x, y, dx, dy):
        """
        Called whenever the mouse moves.
        """
        self.ship_sprite.center_x = x

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called whenever the mouse button is clicked.
        """
        if self.current_state == START:
            self.current_state = GAME_RUNNING
        elif self.current_state == GAME_OVER:
            self.setup()
            self.current_state = GAME_RUNNING

    def on_key_press(self, symbol, modifiers):

        if symbol == arcade.key.RIGHT:
            self.ship_sprite.moving_right = True
        elif symbol == arcade.key.LEFT:
            self.ship_sprite.moving_left = True

        if symbol == arcade.key.SPACE:
            self.ship_sprite.shooting = True

    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.RIGHT:
            self.ship_sprite.moving_right = False
        elif symbol == arcade.key.LEFT:
            self.ship_sprite.moving_left = False

        if symbol == arcade.key.SPACE:
            self.ship_sprite.shooting = False

    def update(self, delta_time):
        """ Movement and game logic """

        if self.current_state == GAME_RUNNING:

            # Call update on all sprites
            ENEMY_LIST.update()
            BULLET_LIST.update()
            # self.bullet_list.update()
            self.ship_list.update()

            # loop through each bullet
            for bullet in BULLET_LIST:

                # Check this bullet to see if it hit a enemy
                hit_list = arcade.check_for_collision_with_list(
                    bullet, ENEMY_LIST
                )

                # If it did, get rid of the bullet
                if len(hit_list) > 0:
                    bullet.kill()

                # For every enemy we hit, add to the score and remove the enemy
                for enemy in hit_list:
                    enemy.kill()
                    self.score += 1

            hit_enemy_list = arcade.check_for_collision_with_list(
                self.ship_sprite, ENEMY_LIST
            )
            if len(hit_enemy_list) > 0:
                self.current_state = GAME_OVER

            if (
                time.perf_counter() - self.last_enemy_create
                > self.enemy_create_delay
            ):
                enemy = Enemy()
                enemy.center_y = -10
                ENEMY_LIST.append(enemy)

                self.last_enemy_create = time.perf_counter()

                self.enemy_count += 1


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()

