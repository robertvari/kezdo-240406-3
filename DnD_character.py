class Character:
    def __init__(self, name, race):
        self.name = name
        self.race = race

        self.HP = 100
        self.armor_class = 1
        self.strength = 10
        self.dexterity = 7
        self.constitution = 10
        self.intelligence = 4
        self.wisdom = 6
        self.charisma = 12
        self.equipment = []

    def character_sheet(self):
        print("-"*50)
        print(f"\tName: {self.name}")
        print(f"\tRace: {self.race}")
        print(f"\tHP: {self.HP}")
        print(f"\tArmor Class: {self.armor_class}")
        print(f"\tStrength: {self.strength}")
        print(f"\tDexterity: {self.dexterity}")
        print(f"\tConstitution: {self.constitution}")
        print(f"\tIntelligence: {self.intelligence}")
        print(f"\tWisdom: {self.wisdom}")
        print(f"\tCharisma: {self.charisma}")
        print(f"\tEquipment: {self.equipment}")
        print("-"*50)

    def attack(self):
        pass

    def buy(self):
        pass

my_hero = Character("Robert", "Human")
my_hero.equipment.append("Magic Sword")
my_hero.character_sheet()

elf = Character("Legolas", "Elf")
elf.character_sheet()