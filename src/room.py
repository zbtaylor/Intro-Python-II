# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, items, n_to=None, s_to=None, e_to=None, w_to=None):
        self.name = name
        self.description = description
        self.items = items

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def list_items(self):
        if len(self.items) == 0:
            return "None."
        elif len(self.items) == 1:
            return self.items[0].name
        else:
            return ", ".join([item.name for item in self.items])

    def item_exists(self, name):
        to_return = {"exists": False, "value": None}
        for item in self.items:
            if item.name == name:
                to_return["exists"] = True
                to_return["value"] = item
        return to_return

    def inspect(self, name):
        item = self.item_exists(name)
        if item["exists"] == True:
            item["value"].describe()
        else:
            raise ValueError
