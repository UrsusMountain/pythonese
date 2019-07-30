class Settings:
    def __init__(self):
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(230,230,230)
        self.ship_limit = 3
        self.bullet_width=2
        self.bullet_height=6
        self.bullet_color=(60,60,60)
        self.bullets_allowed=100
        self.fleet_drop_speed=8
        self.speedup_scale=1.1
        self.score_scale=1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor=6.5
        self.bullet_speed_factor = 8
        self.alien_speed_factor = 1.5
        # fleet_direction=为1表示向右移，为-1表示向左移动
        self.fleet_direction = 1
        self.alien_points=50
    def increase_speed(self):
        self.ship_speed_factor*=self.speedup_scale
        self.bullet_speed_factor*=self.speedup_scale
        self.alien_speed_factor*=self.speedup_scale
        self.alien_points=int(self.alien_points*self.score_scale)
