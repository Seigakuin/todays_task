import pgzrun

pgzrun.go()
import random
from pgzero.actor import Actor
from pgzero.game import screen
from pgzero.keyboard import keyboard

WIDTH = 600
HEIGHT = 500
TITLE = "Alien Invasion"

# The Launcher
ship = Actor("ship")
ship.pos = WIDTH // 2, HEIGHT - 50
ship_speed = 2

# The Asteroid
ASTEROID_SIZE = 50, 46
asteroid = Actor("enemy")
asteroid.pos = (
    random.randint(ASTEROID_SIZE[0] / 2, WIDTH - (ASTEROID_SIZE[0] / 2)),
    ASTEROID_SIZE[1],
)
asteroid_speed = 1

# The Missile
MISSILE_SIZE = 20, 43
missile = Actor("laser")
missile.pos = 0, 0
missile_speed = 10
missile_status = 0

game_status = 0
game_score = 0


def draw():
    if game_status == 0:
        screen.draw.text("Press ENTER to start", (100, 300), color="white",
                         fontsize=32)
    if game_status == 1:

        screen.clear()
        screen.draw.text(
                "Score: " + str(game_score), (WIDTH - 100, 50), color="blue",
                fontsize=24
        )
        ship.draw()

        move_asteroid()
        asteroid.draw()

        if missile_status > 0:
            move_missile()
            missile.draw()

        detect_hits()


def update():
    global game_status, game_score, missile_status, asteroid_speed

    if game_status == 0:
        if keyboard.RETURN:
            game_status = 1
            asteroid.pos = (
                random.randint(ASTEROID_SIZE[0] / 2,
                               WIDTH - (ASTEROID_SIZE[0] / 2)),
                ASTEROID_SIZE[1],
            )
            game_score = 0
            asteroid_speed = 1
    elif game_status == 1:
        if keyboard.right:
            move_ship(ship_speed)
        if keyboard.left:
            move_ship(-1 * ship_speed)

        if missile_status == 0:
            if keyboard.space:
                missile.pos = (ship.x, HEIGHT - 50)
                missile_status = 1


def move_ship(distance):
    newpos = ship.x + distance
    if newpos < 50:
        newpos = 50
    elif newpos > WIDTH - 50:
        newpos = WIDTH - 50
    ship.x = newpos


def move_asteroid():
    global game_status
    asteroid.pos = (asteroid.x, asteroid.y + asteroid_speed)


def move_missile():
    global missile_status
    if missile_status > 0:
        missile.pos = (missile.x, missile.y - missile_speed)
        if missile.y < 10:
            missile_status = 0


def detect_hits():
    global game_status, game_score, missile_status, asteroid_speed
    if asteroid.y >= HEIGHT - (ASTEROID_SIZE[1] / 2):
        screen.draw.text("Game Over", (100, 100), color="red", fontsize=32)
        game_status = 0

    if missile_status == 1 and asteroid.collidepoint(missile.pos):
        hit_asteroid()
        missile_status = 0
        asteroid_speed += 1
        game_score += 1


def hit_asteroid():
    asteroid.pos = (
        random.randint(ASTEROID_SIZE[0] / 2, WIDTH - (ASTEROID_SIZE[0] / 2)),
        ASTEROID_SIZE[1],
    )
