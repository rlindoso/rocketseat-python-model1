import random
# Character: Main class
# Hero: Controled by user
# Enemy: User`s Adversary

class Character:
    def __init__(self, name, life, level) -> None:
        self.__name = name
        self.__life = life
        self.__level = level

    def get_name(self):
        return self.__name

    def get_life(self):
        return self.__life

    def get_level(self):
        return self.__level
    
    def show_detail(self):
        return f"\nName: {self.get_name()}\nLife: {self.get_life()}\nLevel: {self.get_level()}"
    
    def attack(self, target):
        damage = random.randint(self.get_level() * 2, self.get_level() * 4)
        target.hitted(damage)
        print(f"\n{self.get_name()} attacked {target.get_name()} and hit {damage} of damage!")

    def hitted(self, damage):
        self.__life -= damage
        if self.__life < 0:
            self.__level = 0

class Hero(Character):
    def __init__(self, name, life, level, ability) -> None:
        super().__init__(name, life, level)
        self.__ability = ability

    def get_ability(self):
        return self.__ability
    
    def show_detail(self):
        return f"{super().show_detail()}\nAbility: {self.get_ability()}"
    
    def special_attack(self, target):
        damage = random.randint(self.get_level() * 5, self.get_level() * 8)
        target.hitted(damage)
        print(f"\n{self.get_name()} attacked {target.get_name()} with special attack {self.__ability} and hit {damage} of damage!")
    
class Enemy(Character):
    def __init__(self, name, life, level, type) -> None:
        super().__init__(name, life, level)
        self.__type = type

    def get_type(self):
        return self.__type
    
    def show_detail(self):
        return f"{super().show_detail()}\nType: {self.get_type()}"
    
class Game:
    """ Game controller """
    def __init__(self) -> None:
        self.hero = Hero(name="Hero", life=100, level=5, ability="Super power")
        self.enemy = Enemy(name="Bat", life=50, level=3, type="Flyer")

    def start_battle(self):
        print("Start battle!")
        while self.hero.get_life() > 0 and self.enemy.get_life() > 0:
            print("\nCharacters detail:")
            print(self.hero.show_detail())
            print(self.enemy.show_detail())

            input("Press enter to attack...")
            choice = input("Choose (1 - Normal Attack, 2 - Special Attack): ")

            if choice == "1":
                self.hero.attack(self.enemy)
            elif choice == "2":
                self.hero.special_attack(self.enemy)
            else:
                print("Wrong choice! Choose again.")
            
            if self.enemy.get_life() > 0:
                self.enemy.attack(self.hero)

        if self.hero.get_life() > 0:
            print("\nCongratilations! You won!!")
        else:
            print("\nYou was defeated")



game = Game();
game.start_battle()