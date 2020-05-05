import os
import yaml

class Test01:
    def __init__(self):
        self._name = 15
    @property
    def name(self):
        return self._name

t = Test01()
t.name = 16
print(t.name)