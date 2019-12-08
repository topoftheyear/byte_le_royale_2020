import cocos
import pyglet
import os
import shutil
from zipfile import ZipFile
from PIL import Image
from io import BytesIO

# Extracts a png from a zipped file and returns it for use with cocos.
# This function is necessary for the visualizer to work on Linux.
def find_image(filename):
    archive = ZipFile("launcher.pyz", 'r')
    img = Image.open(BytesIO(archive.read(filename)))

    if not os.path.exists('tempic'):
        os.mkdir('tempic')
    img.save('tempic/tempimg.png')
    pic = pyglet.image.load('tempic/tempimg.png')
    shutil.rmtree('tempic')
    return pic

# Populates a dictionary with all the sprites required for the visualizer
def load(temp):
    assets = temp
    plains = cocos.sprite.Sprite(find_image("game/visualizer/assets/location_assets/location_plains.png"))
    assets['location'] = {
        "0": plains
    }

    city_0 = cocos.sprite.Sprite(find_image("game/visualizer/assets/city_assets/city_level0.png"))
    city_1 = cocos.sprite.Sprite(find_image("game/visualizer/assets/city_assets/city_level1.png"))
    city_2 = cocos.sprite.Sprite(find_image("game/visualizer/assets/city_assets/city_level2.png"))
    city_3 = cocos.sprite.Sprite(find_image("game/visualizer/assets/city_assets/city_level3.png"))
    assets['city'] = {
        "0": city_0,
        "1": city_1,
        "2": city_2,
        "3": city_3
    }

    dis_fire = cocos.sprite.Sprite(find_image("game/visualizer/assets/disaster_assets/fire.png"))
    dis_tornado = cocos.sprite.Sprite(find_image("game/visualizer/assets/disaster_assets/tornado.png"))
    dis_hurricane = cocos.sprite.Sprite(find_image("game/visualizer/assets/disaster_assets/hurricane.png"))
    dis_earthquake = cocos.sprite.Sprite(find_image("game/visualizer/assets/disaster_assets/earthquake.png"))
    dis_monster = cocos.sprite.Sprite(find_image("game/visualizer/assets/disaster_assets/monster.png"))
    dis_ufo = cocos.sprite.Sprite(find_image("game/visualizer/assets/disaster_assets/ufo.png"))
    assets['disaster'] = {
        "fire": dis_fire,
        "tornado": dis_tornado,
        "hurricane": dis_hurricane,
        "earthquake": dis_earthquake,
        "monster": dis_monster,
        "ufo": dis_ufo
    }

    assets['forecast'] = {}
    assets['forecast']['fire'] = list()
    assets['forecast']['tornado'] = list()
    assets['forecast']['hurricane'] = list()
    assets['forecast']['earthquake'] = list()
    assets['forecast']['monster'] = list()
    assets['forecast']['ufo'] = list()
    assets['forecast']['clear'] = list()
    for i in range(5):
        fore_fire = cocos.sprite.Sprite(find_image("game/visualizer/assets/forecast_assets/tape_fire.png"))
        fore_tornado = cocos.sprite.Sprite(find_image("game/visualizer/assets/forecast_assets/tape_tornado.png"))
        fore_hurricane = cocos.sprite.Sprite(find_image("game/visualizer/assets/forecast_assets/tape_hurricane.png"))
        fore_earthquake = cocos.sprite.Sprite(find_image("game/visualizer/assets/forecast_assets/tape_earthquake.png"))
        fore_monster = cocos.sprite.Sprite(find_image("game/visualizer/assets/forecast_assets/tape_monster.png"))
        fore_ufo = cocos.sprite.Sprite(find_image("game/visualizer/assets/forecast_assets/tape_ufo.png"))
        fore_clear = cocos.sprite.Sprite(find_image("game/visualizer/assets/forecast_assets/tape_clear.png"))
        assets['forecast']['fire'].append(fore_fire)
        assets['forecast']['tornado'].append(fore_tornado)
        assets['forecast']['hurricane'].append(fore_hurricane)
        assets['forecast']['earthquake'].append(fore_earthquake)
        assets['forecast']['monster'].append(fore_monster)
        assets['forecast']['ufo'].append(fore_ufo)
        assets['forecast']['clear'].append(fore_clear)


    # Sensor Images and Dictionaries
    fire_alarm = find_image("game/visualizer/assets/sensor_assets/fire_alarm.png")
    fire_alarm_grid = pyglet.image.ImageGrid(fire_alarm, 1, 2)

    fire_alarm_level_0 = cocos.sprite.Sprite(pyglet.image.Animation.from_image_sequence(fire_alarm_grid[0::], 0.1))
    fire_alarm_level_1 = cocos.sprite.Sprite(pyglet.image.Animation.from_image_sequence(fire_alarm_grid[0::], 0.1))
    fire_alarm_level_2 = cocos.sprite.Sprite(pyglet.image.Animation.from_image_sequence(fire_alarm_grid[0::], 0.1))
    fire_alarm_level_3 = cocos.sprite.Sprite(pyglet.image.Animation.from_image_sequence(fire_alarm_grid[0::], 0.1))

    sensor_1 = cocos.sprite.Sprite(find_image("game/visualizer/assets/sensor_assets/fire_alarm.png"))
    sensor_2 = cocos.sprite.Sprite(find_image("game/visualizer/assets/sensor_assets/fire_alarm.png"))
    sensor_3 = cocos.sprite.Sprite(find_image("game/visualizer/assets/sensor_assets/fire_alarm.png"))
    sensor_4 = cocos.sprite.Sprite(find_image("game/visualizer/assets/sensor_assets/fire_alarm.png"))
    sensor_5 = cocos.sprite.Sprite(find_image("game/visualizer/assets/sensor_assets/fire_alarm.png"))

    assets['sensor'] = {
        "fire_alarm": {
              "0": fire_alarm_level_0,
              "1": fire_alarm_level_1,
              "2": fire_alarm_level_2,
              "3": fire_alarm_level_3,
                },
        "1": sensor_1,
        "2": sensor_2,
        "3": sensor_3,
        "4": sensor_4,
        "5": sensor_5,
    }

    decree_0 = cocos.sprite.Sprite(find_image("game/visualizer/assets/decree_assets/anti_fire_dogs.png"))
    decree_1 = cocos.sprite.Sprite(find_image("game/visualizer/assets/decree_assets/paperweights.png"))
    decree_2 = cocos.sprite.Sprite(find_image("game/visualizer/assets/decree_assets/snow_shovels.png"))
    decree_3 = cocos.sprite.Sprite(find_image("game/visualizer/assets/decree_assets/rubber_boots.png"))
    decree_4 = cocos.sprite.Sprite(find_image("game/visualizer/assets/decree_assets/fishing_hook.png"))
    decree_5 = cocos.sprite.Sprite(find_image("game/visualizer/assets/decree_assets/cheese.png"))
    decree_default = cocos.sprite.Sprite(find_image("game/visualizer/assets/decree_assets/decree_default.png"))
    assets['decree'] = {
        "-1": decree_default,
        "0": decree_0,
        "1": decree_1,
        "2": decree_2,
        "3": decree_3,
        "4": decree_4,
        "5": decree_5
    }

    wrkr = find_image("game/visualizer/assets/worker.png")
    wrkr_grid = pyglet.image.ImageGrid(wrkr, 1, 48)

    assets['worker'] = {}

    assets['worker']['normal'] = list()
    wrkr_normal = pyglet.image.Animation.from_image_sequence(wrkr_grid[0:15:], 0.1)
    for x in range(50):
        sprite = cocos.sprite.Sprite(
            wrkr_normal,
        )
        assets['worker']['normal'].append(sprite)

    assets['worker']['hammer'] = list()
    wrkr_hammer = pyglet.image.Animation.from_image_sequence(wrkr_grid[16:23:], 0.1)
    for x in range(50):
        sprite = cocos.sprite.Sprite(
            wrkr_hammer,
        )
        assets['worker']['hammer'].append(sprite)

    assets['worker']['money'] = list()
    wrkr_money = pyglet.image.Animation.from_image_sequence(wrkr_grid[24:31:], 0.1)
    for x in range(50):
        sprite = cocos.sprite.Sprite(
            wrkr_money,
        )
        assets['worker']['money'].append(sprite)

    assets['worker']['pick'] = list()
    wrkr_pick = pyglet.image.Animation.from_image_sequence(wrkr_grid[32:39:], 0.1)
    for x in range(50):
        sprite = cocos.sprite.Sprite(
            wrkr_pick,
        )
        assets['worker']['pick'].append(sprite)

    assets['worker']['phone'] = list()
    wrkr_phone = pyglet.image.Animation.from_image_sequence(wrkr_grid[40:47:], 0.1)
    for x in range(50):
        sprite = cocos.sprite.Sprite(
            wrkr_phone,
        )
        assets['worker']['phone'].append(sprite)
    return assets