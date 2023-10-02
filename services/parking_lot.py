from constants import VehicleType
from models.floor import Floor
from models.parking_lot import ParkingLot
from resolvers.slot import SlotResolver


class ParkingLotService:
    def create(self, id, no_of_floors, no_of_slots):
        floor_objs = []
        for floor in range(no_of_floors):
            slot_objs = []
            for slot in range(no_of_slots):
                if slot == 0:
                    slot_type = VehicleType.TRUCK
                elif slot == 1:
                    slot_type = VehicleType.BIKE
                else:
                    slot_type = VehicleType.CAR
                slot_class = SlotResolver.get_obj(slot_type=slot_type)
                slot_obj = slot_class(id=slot, floor=floor, type=slot_type, is_occupied=False).create()
                slot_objs.append(slot_obj)
            floor_obj = Floor(id=floor, slots=slot_objs)
            floor_objs.append(floor_obj)
        parking_lot = ParkingLot(id=id, floors=floor_objs)
        return parking_lot
