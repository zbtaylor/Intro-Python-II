class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_get(self):
        print(f'You have picked up {self.name}.')

    def on_drop(self):
        print(f'You have dropped {self.name}.')

    def describe(self):
        print(self.description)
