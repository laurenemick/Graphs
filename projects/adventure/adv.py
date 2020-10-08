from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
import os

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "/Users/adrienneemick/Desktop/Lambda/web32cs/Graphs/projects/adventure/maps/test_line.txt"
# map_file = "/Users/adrienneemick/Desktop/Lambda/web32cs/Graphs/projects/adventure/maps/test_cross.txt"
# map_file = "/Users/adrienneemick/Desktop/Lambda/web32cs/Graphs/projects/adventure/maps/test_loop.txt"
# map_file = "/Users/adrienneemick/Desktop/Lambda/web32cs/Graphs/projects/adventure/maps/test_loop_fork.txt"
map_file = '/Users/adrienneemick/Desktop/Lambda/web32cs/Graphs/projects/adventure/maps/main_maze.txt'

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
graph = {}
graph[player.current_room] = {'n': '?', 's': '?', 'w': '?', 'e': '?'}

# while there are rooms to be visited 
while len(graph) < len(room_graph):
    # picks a random unexplored direction from the player's current room
    for direction in graph[player.current_room.id]:
    # travels and logs that direction
    # then loops
    # When you reach a dead-end (i.e. a room with no unexplored paths), walk back to the nearest room that does contain an unexplored path

    # You can find the path to the shortest unexplored room by using a breadth-first search for a room with a `'?'` for an exit.


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



# #######
# # UNCOMMENT TO WALK AROUND
# #######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
