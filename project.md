---

# Dungeon and Dragons 8-)

in this project we have an OOP instance of the game called "DandD" the whole project contains 7 py files which are the basics of our project and our classes are implemented within the files.

---

## Shop.py

we have a class called shop in the shop.py file which is all about the shop inside the game where you have buy different things and even use some methods to add items to shop you can see and show the shop to user.

---

## Monster.py

Here we have a super class called Monster and 5 sub classes ( which are different kind of monsters including wold dragon bandit troll and giant ) whom inherited from the Monster class. the purpose of this file in the project is we randomly generate a monster which has a health a gold and a specific damage which can be dealt to player.

---

## Map.py

we have file called map.py which has a class named MapGrid in it. the purpose of this class is to generate the field in the game which we can see during the game. it also specifies the location of ( player, shop, door, walls, start location) and you can choose the width and the height of the grid here in this class. it also has a method which you can generate random walls like a maze in the map which player can not cross.

---

## SignupLogin.py and User_class.py

Main file for register or login user into the game which is pretty simple and we are using another class called User_class.py which is the main class. in the first class we take the inputs from user and we check them with the methods of the second class to validate the user information.

---

## game.py

the main file and the most important file in our project is the game file. this file is the logic behind the game which we can say it is the engine of our project. we have many different methods in this file. the main class here in this file called the Player class. here we can play the game . it specifies if the player wants to move, rest, attack the monsters, finish the game, use the shop and ...
the whole game is implemented in this class

---

## main.py

the main class which we run to start the game. it uses all other classes in our folder to run the game.

---

## The dungeon and dragons

Now its time to explain how the game works:
after we run the project we need to login or register as a user which is easy as a cake
after registering we need to login and then we enter the main menu of our game.
we have a menu consisting of many options like :
inventory, move, rest, scavenge, use, log out, help.
we go through them one by one. the inventory option is for showing what uou have with you at the start of the game which includes an apple and an old knife. if we purchase something from the shop it goes to our inventory and with using our "use" option we can use objects in our inventory. for example if we use apple we get heal for a logical random number.
login out option is pretty easy to understand it just logs you out and you can not continue playing the game and you need to login again.
the move option which is the most important option is going to show you the field or the map of the game. green squares are the ones you are allowed to move into and the red ones are the ones you can not cross. you a start in the map which is the player and a shop in the middle of the map and a finishing point and the end of the map which is the door. the mission is to get gold in the game to buy the key from the shop and enter the door to win the game.
but how do you get golds? there is an option which is called "Scavenging" which you can use when you are in the main menu or when you are moving around in the map. you get a random number of gold which is between 1 to 4 or you may even not get gold at all in a single turn.
but you need to be aware that the turns are not there to move on ! after a random number of turns the monsters are gonna attack you. you will be noticed when they do! if they attacked you you have no option left. you need to fight them. you can not go to menu you can not log out. you have the fight them until one of you lives. then one of you will die! if its the monster you will get 15 gold from it and if its you, .....
you can use rest option to get healed but its not that much so you might need something stronger which you can purchase 2 kind of health potion from the shop. but consider 2 things: you need to move to the shop to be able to buy them and the monsters may attack you when you are moving towards it.
the objective is to collect 100 gold and buy the key from the shop and then go to the door and finish the game :) good luck playing it

---
