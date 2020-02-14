from typing import Union, Dict
from .room import Room


class RoomManager:
    rooms: Union[Dict, Room]

    def __init__(self):
        self.rooms = {}

    def save(self, room: Room):
        if room.name in self.rooms:
            raise ValueError(f"{room.name} already exists!")
        else:
            self.rooms[room.name] = room
