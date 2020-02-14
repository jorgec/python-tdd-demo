class Room:
    # Fields
    name: str
    __capacity: int

    @property
    def capacity(self) -> int:
        return self.__capacity

    @capacity.setter
    def capacity(self, n: int) -> None:
        if n < 10 or n > 50:
            raise ValueError(f"{n} is out of bounds!")
        self.__capacity = n

    def __init__(self, name: str):
        self.name = name
        self.capacity = 10
