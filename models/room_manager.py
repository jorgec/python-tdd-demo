from models.room import Room


class RoomManager:
    rooms: dict

    def __init__(self):
        self.rooms = {}
        self.model = Room

    def save(self, instance: object):
        if instance.name in self.rooms:
            raise ValueError(f"Room with name {instance.name} already exists!")
        self.rooms[instance.name] = instance
