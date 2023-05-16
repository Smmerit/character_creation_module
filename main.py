# .../Dev/character_creation_module/main.py

# Импортируем функцию стандартного модуля random.
from random import randint


class Character:

    def __init__(self, name):
        self.name = name
    
    def attack(self):
        # Описываем метод атаки.
        return (f'{self.name} нанёс противнику урон, равный '
                f'{5 + randint(5, 10)}')
    
    def defence(self):
        ...

    def special(self):
        ...

class Warrior(Character):
    ...

class Mage(Character):
    ...

class Healer(Character):
    ...
