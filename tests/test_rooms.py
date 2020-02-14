import pytest
import random
from faker import Faker
from models.room import Room
from models.room_manager import RoomManager

fake = Faker()


def test_room_creation():
    room = Room(name="Room 1")
    assert room.name == "Room 1"


def test_room_unique_identifier():
    name = fake.name()
    room1 = Room(name=name)
    room2 = Room(name=name)

    room_manager = RoomManager()
    room_manager.save(room1)

    assert len(room_manager.rooms) == 1

    with pytest.raises(ValueError):
        room_manager.save(room2)

    assert len(room_manager.rooms) == 1


def test_room_variable_capacity():
    name = fake.name()
    room = Room(name=name)

    cap = random.randint(10, 50)

    assert room.capacity >= 10

    room.capacity = cap

    assert room.capacity == cap


def test_room_capacity_bounds():
    name = fake.name()
    room = Room(name=name)

    with pytest.raises(ValueError):
        room.capacity = 5
