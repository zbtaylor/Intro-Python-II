# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, current_room, items):
        self.current_room = current_room
        self.items = items

    def move(self, direction):
        try:
            if direction == 'n':
                self.current_room = self.current_room.n_to
                print("You move North.")
            if direction == 's':
                self.current_room = self.current_room.s_to
                print("You move South.")
            if direction == 'e':
                self.current_room = self.current_room.e_to
                print("You move East.")
            if direction == 'w':
                self.current_room = self.current_room.w_to
                print("You move West.")
        except:
            print("There is nothing in that direction.")

    def add_item(self, name):
        item = self.current_room.item_exists(name)
        if item["exists"] == True:
            self.items.append(item["value"])
            self.current_room.remove_item(item["value"])
            item["value"].on_get()
        else:
            raise ValueError

    def remove_item(self, name):
        try:
            for item in self.items:
                if item.name == name:
                    self.items.remove(item)
                    self.current_room.add_item(item)
                    item.on_drop()
        except:
            raise ValueError

    def list_items(self):
        if len(self.items) == 0:
            return "You have no items."
        elif len(self.items) == 1:
            return self.items[0].name
        else:
            return ", ".join([item.name for item in self.items])
