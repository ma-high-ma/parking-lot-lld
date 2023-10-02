class Slot:
    def __init__(self, id, floor, type, is_occupied):
        self.id = id
        self.floor = floor
        self.type = type
        self.is_occupied = is_occupied

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def set_floor(self, floor):
        self.floor = floor

    def get_floor(self):
        return self.floor

    def set_type(self, type):
        self.type = type

    def get_type(self):
        return self.type

    def set_is_occupied(self, is_occupied):
        self.is_occupied = is_occupied

    def get_is_occupied(self):
        return self.is_occupied
