class Floor:
    def __init__(self, id, slots):
        self.id = id
        self.slots = slots

    def set_slots(self, slots):
        self.slots = slots

    def get_slots(self):
        return self.slots

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id
