from typing import List


class Bin:

    def __init__(self) -> None:
        self.__items = []
        self.__cap_taken = 0

    def add(self, element: int):
        self.__items.append(element)
        self.__cap_taken += element

    @property
    def elements(self) -> List[int]:
        return self.__items

    @property
    def cap_taken(self) -> int:
        return self.__cap_taken
