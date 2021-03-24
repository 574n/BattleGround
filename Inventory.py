
class Inventory(object):
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        self.items[item] += 1

    def drop_item(self, item):
        if (item.name in self.items) and (self.items[item] != 0):
            self.items[item] -= 1
        else:
            del self.items[item]

    def use_item(self, item, target=None):
        if item in self.items.values():
            item.use_item(target)

    def __str__(self):
        out = '\t'.join(['Наименование предмета', 'Уровень предмета', 'Используемый?', 'Ловкость', 'Защита',
                         'Здоровье','Тип', 'Подтип', 'Сила ' ])
        for item in self.items.values():
            out += '\n' + '\t'.join([str(x) for x in ([item.name, item.exp, item.applied,
                                                    item.dexterity, item.protection, item.health, item.item_type,
                                                      item.sub_type, item.strenght])])
        return out
