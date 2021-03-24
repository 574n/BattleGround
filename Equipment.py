class Equipment:
    def __init__(self,inventory):
        self.inventory = inventory
        self.head = None
        self.chest = None
        self.belt = None
        self.legs = None
        self.first_weapon = None
        self.trinket = None



    def takeoff_item(self,slot):
        if slot == 'head':
            self.inventory.add_item(self.head)
            self.head = None
        elif slot == 'chest':
            self.inventory.add_item(self.chest)
            self.chest = None
        elif slot == 'belt':
            self.inventory.add_item(self.belt)
            self.belt = None
        elif slot == 'legs':
            self.inventory.add_item(self.legs)
            self.legs = None
        elif slot == 'first_weapon':
            self.inventory.add_item(self.first_weapon)
            self.first_weapon = None
        elif slot == 'trinket':
            self.inventory.add_item(self.trinket)
            self.trinket = None
        elif slot == 'all':
            for slot_iter in ('head','chest','belt','legs','first_weapon','trinket'):
                self.takeoff_item(slot_iter)

    def equip(self, item):
        if item.slot == "head":
            self.takeoff_item("head")
            self.head = item
        elif item.slot == "chest":
            self.takeoff_item("chest")
            self.chest = item
        elif item.slot == "belt":
            self.takeoff_item("belt")
            self.belt = item
        elif item.slot == "legs":
            self.takeoff_item("legs")
            self.legs = item
        elif item.slot == "first_weapon":
            self.takeoff_item("first_weapon")
            self.first_weapon = item
        elif item.slot == "trinket":
            self.takeoff_item("trinket")
            self.trinket = item
        self.inventory.drop_item(item)

