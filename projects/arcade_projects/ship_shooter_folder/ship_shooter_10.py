"""Spaceship Shooter Game 10 - 左右キーでShipを動かす

Goal:
    - Shipを左右キーで物理に基づき、動くようにする

Ship に acceleration_x を追加
Ship - update() を物理法則に基づいてアルゴリズムを書く
on_mouse_motionを消す

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

# Bulletを格納するリスト
BULLET_LIST = arcade.SpriteList()

# Enemy を格納するリスト
ENEMY_LIST = arcade.SpriteList()


class Ship(arcade.Sprite):
    def __init__(self):
        super().__init__("./ship.png", SPRITE_SCALING_SHIP)
        self.acceleration_x = 0.0
        self.change_x = 0.0

        self.moving_right = False
        self.moving_left = False

    def update(self):
        # 速度(change_x)に加速(acceleration_x)を足す
        self.change_x += self.acceleration_x
        # 速度(change_x)を位置(center_x)に足す
        self.center_x += self.change_x
        # 加速(acceleration_x)を0に戻す
        self.acceleration_x *= 0.0

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
            self.acceleration_x += 0.5
            # self.apply_force(0.5)
        elif self.moving_left:
            self.acceleration_x -= 0.5
            # self.apply_force(-0.5)


class Enemy(arcade.Sprite):
    def __init__(self):
        super().__init__("./enemy.png", SPRITE_SCALING_ENEMY)
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
        self.background = arcade.load_texture("./background.png")

    def on_draw(self):
        """Render the screen.
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
        ENEMY_LIST.draw()
        self.ship_list.draw()
        BULLET_LIST.draw()

        # Render the text
        arcade.draw_text(
                f"Score: {self.score}", 10, 20, arcade.color.WHITE, 14
        )

    def on_mouse_motion(self, x, y, dx, dy):
        """
        Called whenever the mouse moves.
        """
        # self.ship_sprite.center_x = x
        pass

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called whenever the mouse button is clicked.
        """
        bullet = arcade.Sprite("./laser.png", SPRITE_SCALING_LASER)

        bullet.center_x = self.ship_sprite.center_x
        bullet.center_y = self.ship_sprite.center_y + 30
        bullet.change_y = BULLET_SPEED

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.SPACE:
            bullet = arcade.Sprite("./laser.png", SPRITE_SCALING_LASER)

            bullet.center_x = self.ship_sprite.center_x
            bullet.center_y = self.ship_sprite.center_y + 30
            bullet.change_y = BULLET_SPEED

            # add bullet to list
            BULLET_LIST.append(bullet)

        if symbol == arcade.key.RIGHT:
            self.ship_sprite.moving_right = True
        elif symbol == arcade.key.LEFT:
            self.ship_sprite.moving_left = True

    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.RIGHT:
            self.ship_sprite.moving_right = False
        elif symbol == arcade.key.LEFT:
            self.ship_sprite.moving_left = False

    def update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites
        ENEMY_LIST.update()
        BULLET_LIST.update()
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

            # If the bullet flies off-screen, remove it.
            if bullet.bottom > SCREEN_HEIGHT:
                bullet.kill()


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
