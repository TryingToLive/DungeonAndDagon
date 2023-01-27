import SignupLogin as s
from map import Map_Grid
from map import graph
import game


play = game.Player()
user = s.Login()
user.Welcome()
graph.walls = Map_Grid.get_walls(graph)
play.help()
play.play()
