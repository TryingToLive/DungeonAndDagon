from random import randint


class Monster:
    def __init__(self, health, gold, damage):
        self.maxHealth = health
        self.health = health
        self.gold = int(gold / 2)
        self.damage = damage

    def get_name():
        return "monster"

    def __str__(self):
        return self.get_name() + " with " + self.health + " health"

    def deal_damage(self, who, dmg):
        who.take_damage(dmg)

    def take_damage(self, dmg):

        self.health = self.health - dmg
        print(self.health)
        return self.health

    def heal(self, amount):
        if self.maxHealth - self.health < amount:
            self.health = self.maxHealth
        else:
            self.health += amount

    def die(self):
        if self.health == 0:
            self.die

    def attack(self, target):

        damage = randint(10, 100) / 10
        self.deal_damage(target, damage)
        return damage


class Troll(Monster):
    def __init__(self):
        Monster.__init__(self, 50, 4, 10)

    def get_name(self):
        return "troll"


class Bandit(Monster):
    def __init__(self):
        Monster.__init__(self, 40, 12, 10)

    def get_name(self):
        return "bandit"


class Wolf(Monster):
    def __init__(self):
        Monster.__init__(self, 60, 4, 10)

    def get_name(self):
        return "wolf"


class Giant(Monster):
    def __init__(self):
        Monster.__init__(self, 120, 20, 10)

    def get_name(self):
        return "giant"


class Dragon(Monster):
    def __init__(self):
        Monster.__init__(self, 60, 20, 10)

    def get_name(self):
        return "dragon"


def monster_from_name(name):
    if name == "troll":
        return Troll()
    elif name == "bandit":
        return Bandit()
    elif name == "wolf":
        return Wolf()
    elif name == "giant":
        return Giant()
    elif name == "dragon":
        return Dragon()
    else:
        return Dragon()


monsters = ["troll", "bandit", "wolf", "giant", "dragon"]


def get_monster():
    num = randint(0, 4)
    return monster_from_name(monsters[num])
