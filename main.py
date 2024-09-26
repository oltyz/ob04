from abc import ABC, abstractmethod

# Шаг 1: Абстрактный класс Weapon
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

# Шаг 2: Реализация конкретных типов оружия
class Sword(Weapon):
    def attack(self):
        return "удар мечом"

class Bow(Weapon):
    def attack(self):
        return "выстрел из лука"

# Шаг 3: Класс Fighter
class Fighter:
    def __init__(self, name: str):
        self.name = name
        self.weapon = None  # Оружие по умолчанию отсутствует

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"{self.name} выбирает {self.weapon.__class__.__name__}.")

    def attack(self):
        if self.weapon:
            print(f"{self.name} наносит {self.weapon.attack()}.")
        else:
            print(f"{self.name} не вооружен!")

# Класс Monster
class Monster:
    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health

    def take_damage(self):
        print(f"Монстр {self.name} побежден!")

# Шаг 4: Реализация боя
def battle(fighter: Fighter, monster: Monster):
    if fighter.weapon:
        fighter.attack()
        monster.take_damage()
    else:
        print(f"{fighter.name} не может атаковать без оружия!")

# Пример использования
if __name__ == "__main__":
    # Создаем бойца и монстра
    fighter = Fighter("Боец")
    monster = Monster("Гоблин", 100)

    # Боец выбирает меч
    sword = Sword()
    fighter.change_weapon(sword)
    battle(fighter, monster)

    # Боец меняет оружие на лук
    bow = Bow()
    fighter.change_weapon(bow)
    battle(fighter, monster)
