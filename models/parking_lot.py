class ParkingLot:
    def __init__(self, id, floors):
        self.id = id
        self.floors = floors

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def set_floors(self, floors):
        self.floors = floors

    def get_floors(self):
        return self.floors
