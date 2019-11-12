class Settings:
    """a class to store all settings for Alien Invasion."""

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        self.ship_speed_factor = 30
        self.ship_limit = 2

        self.bullet_speed_factor = 10
        self.bullet_width = 30
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 10

        self.alien_speed_factor = 1
        self.fleet_drop_speed = 50

        self.fleet_direction = 1

        self.speedup_scale = 1.3
        self.score_scale = 1.5

        self.alien_points = 50

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 30
        self.bullet_speed_factor = 10
        self.alien_speed_factor = 1
        self.fleet_direction = 1
        self.bullet_height = 15
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.bullet_height *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
