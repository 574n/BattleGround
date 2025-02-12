from random import choice, randint
import sys, time
import Fight
import Enemy

def typing(lst):
    for character in lst:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.04)
    print("")

class Adventures:

    adventures_list = ["Пещера", "Город", "Логово монстров", "Лагерь разбойников"]

    def __init__(self, player):
        self.player = player
        place = "Логово монстров"
        if place == "Пещера":
            self.cave()
        elif place == "Город":
            self.__init__(self.player)
        elif place == "Логово монстров":
            self.lair()
        elif place == "Лагерь разбойников":
            self.camp()

    def lair(self, enemy = None):
        if enemy is None:
            enemy = Enemy.Enemy(self.player.lvl)
        count = randint(1,10)
        typing("Во время своих путешествий ты набрел на логово монстра: " + enemy.name)
        typing("Здесь обитает " + str(count) + " " + enemy.name)
        def solve_request():
            typing("Что будем делать?")
            print("1) Напасть")
            print("2) Искать приключения дальше")
            print("3) Выбрать другое действие")
            solve = input("> ")
            solves = ['1', '2', '3']
            if solve in solves:
                if solve == '1':
                    for i in range(count):
                        new_enemy = Enemy.Enemy(self.player.lvl)
                        new_enemy.set_name(enemy.name)
                        Fight.Fight(self.player, new_enemy)
                    self.reward()
                    return
                if solve == '2':
                    self.__init__(self.player)
                if solve == '3':
                    return
            else:
                typing("Ты что-то напутал, давай попробуем еще раз.")
                print("-"*30)
                solve_request()
        solve_request()
    
    def reward(self):
        pass