import textwrap
from item import Item
from room import Room
from player import Player


# Items

bread = Item("Bread", "A stale loaf of bread. It is hard to the touch.")
rope = Item("Rope", "It feels strong enough to hold a person or two.")
sword = Item("Sword", "Dried blood tinges the blade as well as the hilt.")
shield = Item("Shield", "A small, dented buckler.")


# Rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons.",
                     []),

    'foyer':    Room("Foyer",
                     """Dim light filters in from the south. Dusty passages run north and east.""",
                     []),

    'overlook': Room("Grand Overlook",
                     """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.""",
                     [rope]),

    'narrow':   Room("Narrow Passage",
                     """The narrow passage bends here from west to north. The smell of gold permeates the air.""", [bread]),

    'treasure': Room("Treasure Chamber",
                     """You've found the long-lost treasure chamber! Sadly, aside from a few old items, it has already been emptied by earlier adventurers. The only exit is to the south.""",
                     [sword, shield]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(room["outside"], [])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

is_playing = True


def parse_player_input(text):
    global player
    global is_playing
    action = text.split(' ')[0]
    if action == "q":
        is_playing = False
        print("Until next time, adventurer...")
    elif action in ['n', 's', 'e', 'w']:
        player.move(action)
    elif action == "get" or action == "take":
        try:
            item_name = text.split(' ')[1]
            player.add_item(item_name)
        except:
            print("Cannot pick up that item.")
    elif action == "drop":
        try:
            item_name = text.split(' ')[1]
            player.remove_item(item_name)
        except:
            print("Cannot drop that item.")
    elif action == "inspect":
        try:
            item_name = text.split(' ')[1]
            player.current_room.inspect(item_name)
        except:
            print("Cannot inspect that item.")
    elif action == "i" or action == "inventory":
        print("Inventory:")
        print(player.list_items())
    else:
        print("I don't know what that means.")


while is_playing:
    print("\n")
    print('----------------------------------------------------')
    print(f'Location: {player.current_room.name}')
    print(f'Items nearby: {player.current_room.list_items()}')
    print('----------------------------------------------------')
    print("\n")
    print(textwrap.fill(player.current_room.description))
    print("\n")
    next_move = input("What would you like to do? ")
    print("\n")
    print("~")
    parse_player_input(next_move)
    print("~")
