#!/bin/python3

class Item:
    def __init__(self, name: str = "", description: str = "", passive: dict = {}):
        self.name = name
        self.description = description
        self.passive = passive

    def __str__(self) -> str:
        return f"{self.name}:{self.description}:{self.passive}"

    def getName(self) -> str: return self.name
