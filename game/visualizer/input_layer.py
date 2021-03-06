import cocos

from game.visualizer.global_stats import GlobalStats


class InputLayer(cocos.layer.Layer):
    is_event_handler = True

    def __init__(self):
        super().__init__()

        self.global_stats = GlobalStats()

        # Label for displaying current playback speed
        self.speed_label = cocos.text.Label(
            f'{1 / self.global_stats.turn_speed:.2f}x',
            font_name='Arial',
            font_size=15,
            anchor_x='center',
            anchor_y='center'
        )
        self.speed_label.position = 1280 - 70, 16
        self.add(self.speed_label)

    def on_key_press(self, key, modifiers):
        # Up arrow, increases playback speed
        if key == 65362:
            self.global_stats.turn_speed = max(0.25, self.global_stats.turn_speed - 0.25)
            self.update_speed_label()
        # Down arrow, decreases playback speed
        elif key == 65364:
            self.global_stats.turn_speed = min(4, self.global_stats.turn_speed + 0.25)
            self.update_speed_label()
        # Z key, skip to end screen
        elif key == 122:
            self.global_stats.turn_num = -1

    def update_speed_label(self):
        self.speed_label.element.text = f'{1/self.global_stats.turn_speed:.2f}x'
