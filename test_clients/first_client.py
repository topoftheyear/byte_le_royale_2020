from game.client.user_client import UserClient
from game.common.enums import *


class Client(UserClient):
    # Variables and info you want to save between turns go here
    def __init__(self):
        super().__init__()
        self.number = 100
        self.SENSOR_DECREE_MAPPINGS = {
            SensorType.fire: DecreeType.anti_fire_dogs,
            SensorType.tornado: DecreeType.paperweights,
            SensorType.blizzard: DecreeType.snow_shovels,
            SensorType.earthquake: DecreeType.rubber_boots,
            SensorType.monster: DecreeType.fishing_hook,
            SensorType.ufo: DecreeType.cheese
        }

    def team_name(self):
        return "Scrimmy Bingus"

    def city_name(self):
        return "Crungy Spingus"

    def city_type(self):
        return CityType.invested

    # This is where your AI will decide what to do
    def take_turn(self, turn, actions, city, disasters):
        #while True:
        #    actions.add_effort("heehee i'm overflowing memory :)", 1)
        actions.add_effort("heehee i'm not doing anything actually", 1)
        actions.add_effort("other action to make it look not funny in the logs", 1093)

        # Set decree
        highest = -1
        highest_sensor = None
        for sensor in city.sensors.values():
            if sensor.sensor_results > highest:
                highest = sensor.sensor_results
                highest_sensor = sensor

        corresponding_decree = self.SENSOR_DECREE_MAPPINGS[highest_sensor.sensor_type]
        actions.set_decree(corresponding_decree)
