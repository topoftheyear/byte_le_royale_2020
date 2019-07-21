from collections import deque

from game.config import *
from game.common.enums import *


class Action:
    def __init__(self):
        self._allocation_list = deque(maxlen=MAX_ALLOCATIONS_ALLOWED_PER_TURN)
        self._decree = None
        self.object_type = ObjectType.action

    def add_effort(self, effort, number):
        # TODO enforce input to match a standard
        self._allocation_list.append([effort, number])

    def set_decree(self, dec):
        # TODO enforce input to match a standard
        self._decree = dec

    def to_json(self):
        data = dict()
        data['effort'] = list(self._allocation_list)
        data['decree'] = self._decree
        data['object_type'] = self.object_type

        return data

    def from_json(self, data):
        self._allocation_list = data["effort"]
        self._decree = data["decree"]
        self.object_type = data["object_type"]
