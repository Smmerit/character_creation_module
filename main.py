from random import randint

class Character:
        # Константа для диапазона очков урона.
    RANGE_VALUE_ATTACK = (1, 3)

    def __init__(self, name):
        self.name = name

    def attack(self):
        # Вместо диапазона записана переменная класса.
        # Оператор * распаковывает передаваемый кортеж.
        value_attack = 5 + randint(*self.RANGE_VALUE_ATTACK)
        return (f'{self.name} нанёс противнику урон, равный {value_attack}')
   
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
