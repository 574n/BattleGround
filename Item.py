from random import choice, randint

class Item:
    item_type: str #тип
    sub_type: str #подтип
    strenght: int #сила
    dexterity: int #ловкость
    protection: int #защита
    health: int #здоровье
    name: str #имя
    exp: int #опыт
    applied: bool

    def __init__(self):
        type_list = ["Шлем", "Нагрудный доспех","Пояс", "Штаны","Оружие","Талисман" ,"Зелье"]
        armor_list = ["Голова", "Пояс" , "Нагрудник", "Штаны", "Обувь","Талисман"]
        weapon_list = ["Меч", "Булава", "Копье", "Лук", "Кинжал"]
        potion_list = ["Зелье улучшения", "Зелье лечения", "Зелье опыта"]
        first_part_weapon_name = ["Мощный", "Острый", "Точный", "Крепкий", "Стальной", "Устрашающий"]
        first_part_armor_name = ["Крепкий", "Удобный", "Гладкий", "Скромный"]
        second_part_name = ["короля драконов", "грязного вора", "бродячего", "зла", "добра", "самурая", "джедая"]

        self.item_type = choice(type_list)
        if self.item_type == "Шлем" or "Нагрудный доспех" or "Пояс" or "Штаны" or "Талисман":
            self.sub_type = choice(armor_list)
            self.name = choice(first_part_armor_name) + " " + self.sub_type + " " + choice(second_part_name)
            self.set_characteristics(randint(0,3),randint(0,5),randint(0,5),0,0)
        elif self.item_type == "Оружие":
            self.sub_type = choice(weapon_list)
            self.name = choice(first_part_weapon_name) + " " + self.sub_type + " " + choice(second_part_name)
            self.set_characteristics(randint(0,5),randint(0,5),0,0,0)

        elif self.item_type == "Зелье":
            self.sub_type = choice(potion_list)
            if self.sub_type == "Зелье улучшения":
                self.set_characteristics(randint(0,3), randint(0,3), randint(0,3), 0,0, True)
            if self.sub_type == "Зелье лечения":
                self.set_characteristics(0,0,0,randint(10, 50),0,True)
            if self.sub_type == "Зелье опыта":
                self.set_characteristics(0,0,0,0,randint(10, 50),True )

    def set_characteristics(self, strenght, dexterity, protection, health, exp, applied=False):
        self.strenght = strenght
        self.dexterity = dexterity
        self.protection = protection
        self.helth = health
        self.exp = exp
        self.applied = applied

    def use_item(self):
        str_effects = ''
        if self.applied == True:
            str_effects = f'Игроком был использован предмет {self.name}, получены бонусные эффекты :'

        else:
            str_effects = f'Предмет {self.name} нельзя использовать'

        return str_effects
