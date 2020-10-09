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
# # # shortest is 2

# map_file = "/Users/adrienneemick/Desktop/Lambda/web32cs/Graphs/projects/adventure/maps/test_cross.txt"
# # # shortest is 14

# map_file = "/Users/adrienneemick/Desktop/Lambda/web32cs/Graphs/projects/adventure/maps/test_loop.txt"
# # # shortest is 14

map_file = "/Users/adrienneemick/Desktop/Lambda/web32cs/Graphs/projects/adventure/maps/test_loop_fork.txt"
# # # shortest is 24

# map_file = '/Users/adrienneemick/Desktop/Lambda/web32cs/Graphs/projects/adventure/maps/main_maze.txt'
# # # shortest is 918

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

# while there are rooms to be visited 
while len(graph) < len(room_graph):
    # if player hasn't been in the room, add it to graph with exits
    if player.current_room.id not in graph:
        graph[player.current_room.id] = {}

        for direction in player.current_room.get_exits():
            # create tuples with each direction and '?' value
            graph[player.current_room.id][direction] = '?'
        # print(f'Graph: {graph}')
        # print()

    # picks a random unexplored direction from the player's current room
    def get_unexplored_direction():
        for direction in graph[player.current_room.id]:
            if graph[player.current_room.id][direction] == '?':
                return direction

    # checks if we have visited all rooms before moving
    if len(graph) == len(room_graph):
        break

    current_unexplored_direction = get_unexplored_direction()
    # if you have a room to explore
    if current_unexplored_direction:
        # save room
        previous_room = player.current_room.id
        # go to the room 
        player.travel(current_unexplored_direction)
        # and add it to path
        traversal_path.append(current_unexplored_direction)
        # give direction a value of room id
        graph[previous_room][current_unexplored_direction] = player.current_room.id
        print(f'traversal path: {traversal_path}')
        print(f'Current room: {player.current_room.id}')
    
        # get opposite path, and backtrack until you find a ? 
        opposite_path = []
        for direction in traversal_path:
            if direction == 'n':
                opposite_path.append('s')
            elif direction == 'w':
                opposite_path.append('e')
            elif direction == 's':
                opposite_path.append('n')
            elif direction == 'e':
                opposite_path.append('w')

        print(f'opposite path: {opposite_path}')
        print(f'Graph: {graph}')

    # otherwise, while backtrack until we find ?
    else:
        while current_unexplored_direction is None and len(opposite_path) > 0:
            # get direction to get to previous room
            backtrack = opposite_path.pop()
            if backtrack is not None:
                # move to next previous room
                player.travel(backtrack)
            # add to path
            traversal_path.append(backtrack)
            # reset current unexplored direction to random available exit
            current_unexplored_direction = get_unexplored_direction()


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



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
