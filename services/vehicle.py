from models.vehicle import Vehicle


class VehicleService:
    def create(self, regno, color, type):
        # Todo add validation for vehicle type
        return Vehicle(type=type, regno=regno, color=color)
