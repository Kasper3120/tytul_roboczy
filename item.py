#!/bin/python3

class Item:
    def __init__(self, name="", description="", passive={}):
        self.name = name
        self.description = description
        self.passive = passive

    def __str__(self):
        return f"{self.name}:{self.description}:{self.passive}"

    def getName(self): return self.name
