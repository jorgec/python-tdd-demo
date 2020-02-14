import pytest
from faker import Faker
from models.room import Room
from models.room_manager import RoomManager

fake = Faker()


def test_room_create():
    name = fake.name()
    room = Room(name=name)

    assert room.name == name


def test_room_with_empty_name():
    with pytest.raises(ValueError):
        room = Room(name='')


def test_room_with_null_name():
    with pytest.raises(TypeError):
        room = Room()


def test_room_save():
    room_manager = RoomManager()

    name = fake.name()
    room = Room(name=name)

    room_manager.save(room)

    assert len(room_manager.rooms) == 1
    assert room_manager.rooms[name] == room


def test_room_duplicate_check():
    room_manager = RoomManager()

    name = fake.name()

    room1 = Room(name=name)
    room2 = Room(name=name)

    room_manager.save(room1)

    with pytest.raises(ValueError):
        room_manager.save(room2)
