import pymunk as pmk
import arcade as ade
from time import sleep

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 400
SCREEN_TITLE = "Learning Arcs"


class GameWindow(ade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        ade.set_background_color(ade.color.WHITE)

    def setup(self):
        self.play = True

        self.g_space = pmk.Space()
        self.g_space.gravity = (0, -500)

        mass = 1
        radius = 30

        moment_cir = pmk.moment_for_circle(mass, 0, radius)
        circle_body = pmk.Body(mass, moment_cir)
        circle_shape = pmk.Circle(circle_body, radius)
        circle_body.position = (560, 300)
        circle_shape.elasticity = 0.98
        circle_shape.friction = 1.0

        circle_shape.type = "circle"  # specifics for displaying
        circle_shape.color = ade.color.CYAN

        # self.segment_body = pmk.Body(body_type=pmk.Body.STATIC) - replace with "space.static_body"
        segment_shape = pmk.Segment(self.g_space.static_body, (50, 50), (590, 0), 2)
        segment_shape.body.position = (0, 0)
        segment_shape.elasticity = 0.98
        segment_shape.friction = 1.0

        segment_shape.type = "segment"
        segment_shape.color = ade.color.GRAY

        segment_shape2 = pmk.Segment(self.g_space.static_body, (300, 120), (590, 130), 2)
        segment_shape2.body.position = (0, 0)
        segment_shape2.elasticity = 0.5
        segment_shape2.friction = 1.0

        segment_shape2.type = "segment"
        segment_shape2.color = ade.color.GRAY

        self.g_space.add(circle_body, circle_shape)
        self.g_space.add(segment_shape, segment_shape2)

    def on_draw(self):
        ade.start_render()

        for shape in self.g_space.shapes:
            (x, y) = shape.body.position
            type = shape.type

            if (type == "circle"):
                ade.draw_circle_filled(x, y, shape.radius, shape.color)

                rx, ry = ade.rotate_point(x + shape.radius, y, x, y, shape.body.angle * (180 / 3.1415))

                ade.draw_line(x, y, rx, ry, ade.color.GRAY, 2)

            if (type == "segment"):
                s_x, s_y = shape.a
                e_x, e_y = shape.b

                ade.draw_line(s_x, s_y, e_x, e_y, shape.color, shape.radius)

    def update(self, delta_time):
        if (self.play):
            self.g_space.step(delta_time)

        for shape in self.g_space.shapes:
            if (shape.body.position.y < -50):
                self.g_space.remove(shape, shape.body)

    def on_key_press(self, key, key_modifiers):
        if (key == ade.key.Q):
            quit()

        if (key == ade.key.SPACE):
            self.play = not self.play

    def on_mouse_press(self, x, y, button, modifiers):
        mass = 1
        radius = 10

        moment_cir = pmk.moment_for_circle(mass, 0, radius)
        circle_body = pmk.Body(mass, moment_cir)
        circle_shape = pmk.Circle(circle_body, radius)
        circle_body.position = (x, y)
        circle_shape.elasticity = 0.98
        circle_shape.friction = 1.0

        circle_shape.type = "circle"
        circle_shape.color = ade.color.CYAN

        self.g_space.add(circle_body, circle_shape)
        print("done")


def main():
    game = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    ade.run()


if __name__ == "__main__":
    main()