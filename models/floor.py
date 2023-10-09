class Floor:
    def __init__(self, id, slot_map):
        self.id = id
        self.slot_map = slot_map

    def set_slot_map(self, slot_map):
        self.slot_map = slot_map

    def get_slot_map(self):
        return self.slot_map

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id
