import User_Class as user
import os
from time import sleep
from termcolor import colored
import msvcrt
import logging
import logging.config

logging.config.fileConfig("loggerConfig.toml", disable_existing_loggers=False)
logger = logging.getLogger(__name__)
gameLog = logging.getLogger("gameLogger")
userLog = logging.getLogger("userLogger")


class Login:
    def __init__(self, *args, **kwargs) -> None:
        self._User_Name = ""

    def SignUpUser(self):
        os.system("cls")
        self._User_Name = input("Please enter your username: ")
        os.system("cls")
        self._Password = input("Please enter your Password: ")

        This_user = user.SignUp(self._User_Name, self._Password)
        userLog.info(f"{self._User_Name} signed up")
        os.system("cls")
        print(colored("Welcome to D&D !!!", "red", "on_green"))
        self.Welcome()

    def return_user(self):
        return self._User_Name

    def loginUser(self) -> bool:
        os.system("cls")
        self._User_Name = input("Please enter your username: ")
        os.system("cls")
        self._Password = input("Please enter your Password: ")

        This_User = user.User(self._User_Name, self._Password)

        if This_User.FindTheUser():
            if This_User.check_password():
                userLog.info(f"{self._User_Name} logged in")
                # return This_User.readUserDetail
                return True

            else:
                print("Username or Password is not Correct!")
                exit(0)
        else:
            print("Username or Password is not Correct!")
            exit(0)

    def Welcome(self) -> bool:
        os.system("cls")
        print(colored("Welcome To DND ! \n", "grey", "on_yellow"))
        sleep(0.75)
        print("1.Login \n2.Signup\n")

        User_Choice = msvcrt.getch()

        if User_Choice == b"1":
            self.loginUser()

        elif User_Choice == b"2":
            self.SignUpUser()

        else:
            raise ValueError("please choose one from above")


login = Login()
