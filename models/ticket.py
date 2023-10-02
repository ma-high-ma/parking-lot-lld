class Ticket:
    def __init__(self, id, parking_lot, slot, vehicle):
        self.id = id
        self.parking_lot = parking_lot
        self.slot = slot
        self.vehicle = vehicle

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def set_parking_lot(self, parking_lot):
        self.parking_lot = parking_lot

    def get_parking_lot(self):
        return self.parking_lot

    def set_slot(self, slot):
        self.slot = slot

    def get_slot(self):
        return self.slot

    def set_vehicle(self, vehicle):
        self.vehicle = vehicle

    def get_vehicle(self):
        return self.vehicle
