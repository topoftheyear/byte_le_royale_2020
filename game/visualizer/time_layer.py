import cocos


class TimeLayer(cocos.layer.Layer):
    def __init__(self, display_size, turn_info, text=0):
        self.turn = text
        self.display = display_size
        self.info = turn_info
        super().__init__()
        team_name_label = cocos.text.Label(
            self.info['player']['team_name'],
            font_name="Comic Sans",
            font_size=32,
            anchor_x="center",
            position=(self.display[0]/2, self.display[1]-100)
        )
        self.add(team_name_label)

        turn_label = cocos.text.Label(
            str(self.turn),
            font_name="Comic Sans",
            font_size=32
        )
        if self.turn < 10:
            turn_label.position = self.display[0]-32, self.display[1] - 50
        elif self.turn < 100:
            turn_label.position = self.display[0]-56, self.display[1] - 50
        else:
            turn_label.position = self.display[0]-80, self.display[1] - 50

        gold = self.info['player']['city']['gold']
        gold_label = cocos.text.Label(
            f"Gold: {gold}",
            font_name="Comic Sans",
            font_size=25,
            color=(255,215,0,255),
            anchor_x="center"
        )
        if gold<10:
            gold_label.position = self.display[0]-32, self.display[1] - 100
        elif gold<100:
            gold_label.position = self.display[0] - 56, self.display[1] - 100
        else:
            gold_label.position = self.display[0] - 80, self.display[1] - 100

        self.add(turn_label)
        self.add(gold_label)

        # # Display actual rates
        # n = 0
        # for key, item in self.info['rates'].items():
        #     n+=1
        #     text = f'{key}: {item}'
        #     label = cocos.text.Label(
        #         text,
        #         font_name="Comic Sans",
        #         font_size=15
        #     )
        #     label.position = 30, self.display[1]-50-30*n
        #     self.add(label)
        #
        # # Display city sensor
        # n = 0
        # for sensor in self.info['player']['city']['sensors'].values():
        #     n += 1
        #     text = f'{sensor["sensor_type"]}: {sensor["sensor_results"]}'
        #     label = cocos.text.Label(
        #         text,
        #         font_name="Comic Sans",
        #         font_size=15
        #     )
        #     label.position = 500, self.display[1]-50-30 * n
        #     self.add(label)
