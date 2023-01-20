from random import randint, choice
import sys
from shop import Shop
import monster
import SignupLogin as s


class MapGrid():
    """in this class we identify the attributes for map grid
    and we init the different variables in the game"""

    def __init__(self, width, height):

        self.width = width
        self.height = height
        self.walls = []
        self.start = (0, 0)
        self.goal = (18, 18)
        self.player = (0, 0)
        self.shop = (9, 9)
        self.dragon = (randint(0, 18), randint(0, 18))

    def move_player(self, move):
        obj = Player()
        x = self.player[0]
        y = self.player[1]
        pos = (x, y)
        self.walls = g.walls
        if move[0] == "r":
            pos = (x + 1, y)
            if x >= 18:
                print("out of range")
                pos = (x, y)
        if move[0] == "l":
            pos = (x - 1, y)
            if x <= 0:
                print("out of range")
                pos = (x, y)
        if move[0] == "u":
            pos = (x, y - 1)
            if y <= 0:
                print("out of range")
                pos = (x, y)
        if move[0] == "d":
            pos = (x, y + 1)
            if y >= 18:
                print("out of range")
                pos = (x, y)
        if pos not in self.walls:
            self.player = pos
        if pos == self.shop:
            Player.browseShop(Player(),"\nWelcome to the shop!")
        if pos == self.dragon:
            print("you hit the dragon !")
            shape = "☠ "
            print("%%-%ds" % 2 % shape, end="")
            sys.exit()
        if pos == self.goal:
            if "The key" in obj.inventory:
                print("You made it to the end")
                sys.exit()
            else:
                print("you need the key to open the door and win the game")
                print("you can buy the key from the shop")

    def draw_grid(self, width=2):
        # self.walls = MapGrid.get_walls(self)
        for y in range(self.height):
            for x in range(self.width):
                if (x, y) in g.walls:
                    symbol = "🟥"
                elif (x, y) == self.shop:
                    symbol = "🏠"
                elif (x, y) == self.player:
                    symbol = "★  "
                elif (x, y) == self.start:
                    symbol = "<  "
                elif (x, y) == self.goal:
                    symbol = "🚩"
                elif (x, y) == self.dragon:
                    symbol = "🟩"
                else:
                    symbol = "🟩"
                print("%%-%ds" % width % symbol, end="")
            print()

    def get_walls(self, pct=0.25) -> list:
        out = []
        for _ in range(int((self.height * self.width * pct) // 2)):
            x = randint(1, self.width - 2)
            y = randint(1, self.height - 2)
            out.append((x, y))
            out.append((x + choice([-1, 0, 1]), y + choice([-1, 0, 1])))
            if (9, 9) in out:
                out.remove((9, 9))
            if (18, 18) in out:
                out.remove((18, 18))
        return out


class Player(MapGrid):
    def __init__(self):
        self.inventory = ["apple", "old knife"]
        self.gold = 10
        self.health = 100
        self.maxHealth = 100
        self.restHeal = 5
        self.turns = 0
        self.alive = True
        self.weapon = ""

    def __str__(self):
        return (
            "health: "
            + self.health
            + ", gold: "
            + self.gold
            + ", inventory: "
            + self.inventory
        )

    def getName(self):
        return "player"

    def die(self):
        self.alive = False
        print("Game Over.")
        sys.exit()

    def dealDamage(self, who, dmg):
        who.takeDamage(dmg)

    def takeDamage(self, dmg):
        self.health -= dmg

    def displayList(self, List):
        for i in range(0, len(List)):
            print(str(i + 1) + ": " + List[i])
    def get_gold(self):
        return self.gold

    def heal(self, amount, announce=True):
        if self.maxHealth - self.health < amount:
            self.health = self.maxHealth
            if announce:
                print("You are at full health now.")
        else:
            self.health += amount
            if announce:
                if amount > 0:
                    print(
                        "\nYou have been restored "
                        + str(amount)
                        + " health.\nYou now have "
                        + str(self.health)
                        + "/"
                        + str(self.maxHealth)
                        + " health."
                    )
                else:
                    print(
                        "\nYou have been drained "
                        + str(-amount)
                        + " health.\nYou now have "
                        + str(self.health)
                        + "/"
                        + str(self.maxHealth)
                        + " health."
                    )

    def equipWeapon(self, item):
        if self.weapon != "":
            self.inventory.append(self.weapon)
        self.weapon = item
        print("You have equipped " + item + "!")

    def attacked(self):
        attacker = monster.getMonster()

        print("________________________________________________\n")
        print("You have been attacked by a " + attacker.getName() + "!")
        print("________________________________________________")

        while attacker.health > 0:
            print("\nYou have " + str(self.health) + " health.")
            print(
                "The "
                + attacker.getName()
                + " has "
                + str(attacker.health)
                + " health.\n"
            )

            print("\n")
            print("*  " + "punch does base dmg " + "10")

            print("*  " + "sword does base dmg 15 ")

            attack = input("<attack>").lower()
            if attack == "punch":
                damage = 10
                self.dealDamage(attacker, damage)
                print(
                    "\nYou dealt "
                    + str(damage)
                    + " damage to the "
                    + attacker.getName()
                    + " using punch !"
                )
            elif attack == "sword":
                damage = 15
                self.dealDamage(attacker, damage)
                print(
                    "\nYou dealt "
                    + str(damage)
                    + " damage to the "
                    + attacker.getName()
                    + " using sword !"
                )

            monsterAttack = attacker.attack(self)

            print(
                "\nThe "
                + attacker.getName()
                + " dealt "
                + str(int(monsterAttack))
                + " damage to you "
            )

            if attacker.health <= 0:
                attacker.die()

                print("\nYou have defeated the " + attacker.getName() + "!")
                self.gold = self.gold + 15
                print("and you got 15 gold from it")

                if self.health <= 0:
                    self.die()
                    break
                break

            print("________________________________________________\n")

            if self.health <= 0:
                self.die()
                break

    def scavenge(self):
        if randint(1, 3) <= 2:
            gold = randint(1, 4)
            print("While scavenging, you find " + str(gold) + " gold.")
            self.gold = self.gold + gold
            return gold
        else:
            if randint(1, 30) == 1:
                print("While scavenging, you find a lesser health potion.")
                self.inventory.append("lesser health potion")
            else:
                print("You find nothing while scavenging.")
                
    def browseShop(self, message):
        print(message)
        gold = self.get_gold()
        print("\nYou have " + str(gold) + " gold.")

        items = Shop.show_item(Shop())
        print(items)

        print("0: exit.")
        # for i in range(0, len(items)):
        #    print(
        #        str(i + 1)
        #        + ": "
        #        + str(items[i][0])
        #        + " costs "
        #        + str(items[i][1])
        #        + " gold."
        #    )
        item = Shop.show_list(Shop())
        buy = ""
        while buy != "0":
            buy = input("\n<buy>")
            while not (buy.isdigit() and int(buy) <= len(item)):
                print("Please enter a valid choice, which may be to exit (0).")
                buy = input("<buy>")

            if int(buy) == 0:
                break

            item = item[int(buy) - 1]

            if self.gold < item[1]:
                print("\nYou don't have enough gold to purchase 1 " + item[0] + ".")
                return

            self.gold -= item[1]

            self.inventory.append(item[0])
            print("\nYou purchased 1 " + item[0] + " for " + str(item[1]) + " gold.")
            self.useItem(len(self.inventory) - 1, item[0], True)
            print("\nNow you have " + str(self.gold) + " gold.")

    def rest(self):
        healing = self.restHeal
        if randint(1, 4) == 1:
            print("\n\tCritical heal!")
            healing *= 2
        self.heal(healing)



    def useItem(self, item, itemName, auto_equip=False):
        if itemName == "apple" and not auto_equip:
            self.heal(12 + randint(0, 10))
        elif itemName == "lesser health potion" and not auto_equip:
            self.heal(16 + randint(0, 10))
        elif itemName == "greater health potion" and not auto_equip:
            self.heal(26 + randint(0, 20))
        elif itemName == "old knife":
            self.equipWeapon("old knife")
        else:
            return
        self.inventory.pop(item)

    def use(self):
        print("\n0: <exit>")
        self.displayList(self.inventory)

        use = input("\n<use>")
        while not use.isdigit():
            print("Please enter a valid item number or exit (0).")
            use = input("<use>")

        use = int(use)
        if use == 0:
            return

        self.useItem(use - 1, self.inventory[use - 1])

    def help(self):
        print("\nWelcome to Dungeons and Dragons! ")
        print("Type 'help' to bring up this menu again.\n")
        print(
            "Commands:\n\thelp (h)\n\tmove (m)\n\tinventory (i)\n\tscavenge (s)\n\trest (r)\n\tuse (u)\n"
        )
        print("Beware of monsters; they will occasionally attack you.\n")

    def showInventory(self):
        print(
            "\ngold: " + str(self.gold) + "\ninventory: " + str(self.inventory) + "\n"
        )

    def moves(self, choice):
        choice = choice.lower()
        if choice == "help":
            self.help()
        elif choice == "inventory" or choice == "i":
            self.showInventory()
        elif choice == "rest" or choice == "r":
            self.rest()
        elif choice == "scavenge" or choice == "s":
            self.scavenge()
        elif choice == "use" or choice == "u":
            self.use()
        elif choice == "move" or choice == "m":
            while True:
                MapGrid.draw_grid(g)
                user_input = input(
                    "Please choose you want to move (l, u, r, d) or (ex) to go to menu : "
                ).lower()
                if user_input == "ex":
                    break
                elif user_input == "s" or user_input == "scavenge":
                    self.scavenge()
                else:
                    g.move_player(user_input)
                    self.turns += 1
                    if self.turns > 6 and randint(0, 4) == 0:
                        self.attacked()

        else:
            print("\nPlease type a valid command such as 'shop'.")
            return False
        return True

    def takeTurn(self):
        self.turns += 1
        print("________________________________________________")

        if self.alive is False:
            self.die()

        choice = input("\n<turn>")
        while not self.moves(choice):
            choice = input("\n<turn>")

        if self.turns > 6 and randint(0, 6) == 0:
            self.attacked()

    def play(self):
        while self.alive is True:
            self.takeTurn()
        print("\n\t You survived " + str(self.turns) + " turns.")


Shop.addItem(Shop(), "lesser health potion", 12)
Shop.addItem(Shop(), "greater health potion", 12)
Shop.addItem(Shop(), "rusty sword", 12)
Shop.addItem(Shop(), "key", 12)
user = s.Login()
user.Welcome()
play = Player()
g = MapGrid(19, 19)
g.walls = MapGrid.get_walls(g)
play.help()
play.play()
