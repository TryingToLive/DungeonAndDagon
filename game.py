import sys
import monster
import logging
from shop import Shop
import SignupLogin as s
from random import randint
from map import Map_Grid
from map import graph
import logging.config

# logging configuration in the project
logging.config.fileConfig("loggerConfig.toml", disable_existing_loggers=False)
logger = logging.getLogger(__name__)
gameLog = logging.getLogger("gameLogger")
userLog = logging.getLogger("userLogger")


class Player(Map_Grid):

    """
    this is the main class in our project. in player class we have
    all attributes and methods regard the player and this is the
    engine of our project.

    """

    def __init__(self) -> None:

        """initialize different variables used in the class"""

        self.inventory: list = ["apple", "old knife"]
        self.gold: int = 10
        self.health: int = 100
        self.maxHealth: int = 100
        self.restHeal: int = 5
        self.turns: int = 0
        self.alive: bool = True
        self.weapon: str = ""
        self.login: bool = True

    def __str__(self) -> str:
        """used to return the gold and health and inventory of the player at the start of the game"""
        return (
            "health: "
            + self.health
            + ", gold: "
            + self.gold
            + ", inventory: "
            + self.inventory
        )

    def get_name(self) -> str:
        return "player"

    def die(self) -> str:
        """if the player dies it ends the game"""
        self.alive = False
        print("Game Over.")
        sys.exit()

    def log_out(self) -> str:
        """if the player logged out, it ends the game"""
        userLog.info(f"player : {user.return_user()} logged out")
        sys.exit("you logged out")

    def deal_damage(self, who, dmg) -> None:
        """it deals a number of damage to someone"""
        who.take_damage(dmg)

    def take_damage(self, dmg) -> int:
        """when player takes damage"""
        gameLog.info(f"player : {user.return_user()} took {dmg} damage")
        self.health -= dmg

    def display_list(self, List) -> list:
        """returns the list of our inventory"""
        for i in range(0, len(List)):
            print(str(i + 1) + ": " + List[i])

    def get_gold(self) -> int:
        """returns the gold that player owns"""
        return self.gold

    def heal(self, amount, announce=True) -> str:
        """heals the player for specific amount. if the player is full hp it just returns the full hp"""
        if self.maxHealth - self.health < amount:
            self.health = self.maxHealth
            if announce:
                print("You are at full health now.")
        else:
            self.health += amount
            if announce:
                if amount > 0:
                    gameLog.info(
                        f"player : {user.return_user()} restored {amount} health"
                    )
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

    def equip_weapon(self, item) -> str:
        """when you use a specific weapon from your inventory"""
        if self.weapon != "":
            self.inventory.append(self.weapon)
        self.weapon = item
        gameLog.info(f"player : {user.return_user()} equipped {item} ")
        print("You have equipped " + item + "!")

    def attacked(self) -> str:
        """when the player gets attacked by a random monster.
        here the player can attack the monster choosing how to do that.
        and also in every round the monster will attack you and decrease your hp"""
        attacker = monster.get_monster()

        print("________________________________________________\n")
        print("You have been attacked by a " + attacker.get_name() + "!")
        print("________________________________________________")
        gameLog.info(
            f"player : {user.return_user()} has been attacked by {attacker.get_name()}"
        )
        while attacker.health > 0:
            print("\nYou have " + str(self.health) + " health.")
            print(
                "The "
                + attacker.get_name()
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
                self.deal_damage(attacker, damage)
                print(
                    "\nYou dealt "
                    + str(damage)
                    + " damage to the "
                    + attacker.get_name()
                    + " using punch !"
                )
                gameLog.info(
                    f"player : {user.return_user()} punched the {attacker.get_name()}"
                )
            elif attack == "sword":
                damage = 15
                self.deal_damage(attacker, damage)
                print(
                    "\nYou dealt "
                    + str(damage)
                    + " damage to the "
                    + attacker.get_name()
                    + " using sword !"
                )
                gameLog.info(
                    f"player : {user.return_user()} used sword to attack the {attacker.get_name()}"
                )

            monsterAttack = attacker.attack(self)

            print(
                "\nThe "
                + attacker.get_name()
                + " dealt "
                + str(int(monsterAttack))
                + " damage to you "
            )

            if attacker.health <= 0:
                attacker.die()
                gameLog.info(
                    f"player : {user.return_user()} defeated the {attacker.get_name()}"
                )
                print("\nYou have defeated the " + attacker.get_name() + "!")
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

    def scavenge(self) -> int:
        """here we have this method for finding gold from the ground and you can do it from the menu and also in the map"""
        if randint(1, 3) <= 2:
            gold = randint(1, 4)
            print("While scavenging, you find " + str(gold) + " gold.")
            self.gold = self.gold + gold
            gameLog.info(
                f"player : {user.return_user()} got {gold} gold while scavenging"
            )
            return gold

        else:
            if randint(1, 30) == 1:
                print("While scavenging, you find a lesser health potion.")
                self.inventory.append("lesser health potion")
            else:
                print("You find nothing while scavenging.")

    def browse_shop(self, message) -> str:
        """we call this method when you go to the shop and you can either by or exit"""
        print(message)
        gold = self.get_gold()
        print("\nYou have " + str(gold) + " gold.")

        items = Shop.show_item(Shop())
        print(items)

        print("0: exit.")

        item = Shop.show_list(Shop())
        buy = ""
        while buy != "0":
            buy = input("\n<buy>")
            while not (buy.isdigit() and int(buy) <= len(item)):
                print("Please enter a valid choice, which may be to exit (0).")
                buy = input("<buy>")

            if int(buy) == 0:
                break

            item: list = item[int(buy) - 1]

            if self.gold < item[1]:
                print("\nYou don't have enough gold to purchase 1 " + item[0] + ".")
                gameLog(
                    f"player : {user.return_user()} tried to buy 1 {item[0]} but didnt have enough gold"
                )
                return

            self.gold -= item[1]

            self.inventory.append(item[0])
            print("\nYou purchased 1 " + item[0] + " for " + str(item[1]) + " gold.")
            gameLog.info(f"player : {user.return_user()} bought {item[0]}")
            self.use_item(len(self.inventory) - 1, item[0], True)
            print("\nNow you have " + str(self.gold) + " gold.")

    def rest(self) -> int:
        """in this method, the player can rest and get healed and you have a small chance to get critical heal"""
        healing: int = self.restHeal
        if randint(1, 4) == 1:
            print("\n\tCritical heal!")
            healing *= 2
        self.heal(healing)
        gameLog.info(f"player : {user.return_user()} healed {healing} after resting")

    def use_item(self, item, itemName, auto_equip=False) -> list:
        """
        when the player wants to use an item exists in the inventory.
        but it also depends if the item is defined autoequip or not

        """
        if itemName == "apple" and not auto_equip:
            self.heal(12 + randint(0, 10))
        elif itemName == "lesser health potion" and not auto_equip:
            self.heal(16 + randint(0, 10))
        elif itemName == "greater health potion" and not auto_equip:
            self.heal(26 + randint(0, 20))
        elif itemName == "old knife":
            self.equip_weapon("old knife")
        else:
            return
        self.inventory.pop(item)

    def use(self) -> str:
        """
        when the player wants to use an item it shows the inventory and plyer can choose

        """
        print("\n0: <exit>")
        self.display_list(self.inventory)

        use: int = input("\n<use>")
        while not use.isdigit():
            print("Please enter a valid item number or exit (0).")
            use = input("<use>")

        use = int(use)
        if use == 0:
            return

        self.use_item(use - 1, self.inventory[use - 1])

    def move_player(self, move) -> tuple:

        """
        when the player wants to move in the map. the player cant move within the walls
        and if the player moves toward the shop it will open the shop for him/her
        and also you can not move further than the size of the map
        and if you move towards the door you need a key to open it and finish the game

        """

        x: int = graph.player[0]
        y: int = graph.player[1]
        pos: tuple = (x, y)
        self.walls = graph.walls
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
        gameLog.info(f"player : {user.return_user()} moved from ({x}, {y}) to {pos}")
        if pos not in self.walls:
            graph.player = pos
        if pos == graph.shop:
            self.browse_shop("\nWelcome to the shop!")
        if pos == graph.goal:
            if "The key" in self.inventory:
                print("You made it to the end")
                gameLog.info(
                    f"player : {user.return_user()} entered the door and finished the game"
                )
                sys.exit()
            print("you need the key to open the door and finish the game")
            print("you can buy the key from the shop")
        gameLog.info(
            f"player : {user.return_user()} entered the door but they dont have the key"
        )

    def help(self) -> str:
        """
        opens the starter of the game or the help menu

        """

        print("\nWelcome to Dungeons and Dragons! ")
        print("Type 'help' to bring up this menu again.\n")
        print(
            "Commands:\n\thelp (h)\n\tmove (m)\n\tinventory (i)\n\tscavenge (s)\n\trest (r)\n\tuse (u)\n\tlog out (l)\n"
        )
        print("Beware of monsters; they will occasionally attack you.\n")

    def show_inventory(self) -> str:

        """
        shows the inventory to the player if player wishes

        """
        print(
            "\ngold: " + str(self.gold) + "\ninventory: " + str(self.inventory) + "\n"
        )

    def moves(self, choice) -> bool:

        """
        gets the choice of player from the menu and acts as ordered

        """

        choice: str = choice.lower()
        if choice == "help":
            self.help()
        elif choice == "inventory" or choice == "i":
            self.show_inventory()
        elif choice == "rest" or choice == "r":
            self.rest()
        elif choice == "scavenge" or choice == "s":
            self.scavenge()
        elif choice == "use" or choice == "u":
            self.use()
        elif choice == "move" or choice == "m":
            while True:
                Map_Grid.draw_grid(graph)
                user_input: str = input(
                    "Please choose you want to move (l, u, r, d) and (s) for scavenging or (ex) to go to menu : "
                ).lower()

                if user_input == "ex":
                    break
                elif user_input == "s" or user_input == "scavenge":
                    self.scavenge()
                else:
                    self.move_player(user_input)
                    self.turns += 1
                    if self.turns > 6 and randint(0, 4) == 0:
                        self.attacked()
        elif choice == "log out" or choice == "l":
            self.log_out()
        else:
            print("\nPlease type a valid command such as 'shop'.")
            return False
        return True

    def take_turn(self) -> int:

        """
        counts the turns that player has played to calculate
        when the monster going to attack the player

        """
        self.turns += 1
        print("________________________________________________")

        if self.alive is False:
            self.die()

        choice = input("\n<turn>")
        while not self.moves(choice):
            choice = input("\n<turn>")

        if self.turns > 6 and randint(0, 6) == 0:
            self.attacked()

    def play(self) -> str:

        """
        if player is not dead, then it can play the game and start counting the trun

        """
        while self.alive is True:
            self.take_turn()
        print("\n\t You survived " + str(self.turns) + " turns.")


user = s.Login()
play = Player()


def main():
    user.Welcome()
    graph.walls = Map_Grid.get_walls(graph)
    play.help()
    play.play()
