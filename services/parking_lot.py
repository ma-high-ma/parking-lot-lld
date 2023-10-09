from constants import VehicleType, SlotType
from models.floor import Floor
from models.parking_lot import ParkingLot
from resolvers.slot import SlotResolver


class ParkingLotService:
    # slotMap = {}
    # def create(self, id, no_of_floors, no_of_slots):
    #     floor_objs = []
    #     for floor in range(no_of_floors):
    #         slot_objs = []
    #         for slot in range(no_of_slots):
    #             if slot == 0:
    #                 slot_type = VehicleType.TRUCK
    #             elif slot == 1:
    #                 slot_type = VehicleType.BIKE
    #             else:
    #                 slot_type = VehicleType.CAR
    #             slot_class = SlotResolver.get_obj(slot_type=slot_type)
    #             slot_obj = slot_class(id=slot, floor=floor, type=slot_type, is_occupied=False).create()
    #             slot_objs.append(slot_obj)
    #         floor_obj = Floor(id=floor, slot_map=slot_objs)
    #         floor_objs.append(floor_obj)
    #     parking_lot = ParkingLot(id=id, floors=floor_objs)
    #     return parking_lot

    def create(self, lot_id, no_of_floors, no_of_slots):
        floors = []
        for floor_index in range(no_of_floors):
            floor_obj = self.createFloor(no_of_slots=no_of_slots, floor_index=floor_index)
            floors.append(floor_obj)
        parking_lot = ParkingLot(id=lot_id, floors=floors)
        return parking_lot


    def createFloor(self, no_of_slots, floor_index):
        """
            Floor -> id, slot_map
            SLotMap = {
                LargeSlot : [<slot_obj1, slot_obj2],
                SmallSlot: [<slot_obj3, slot_obj4]
            }
        """
        slot_map = {}
        for slot_index in range(no_of_slots):
            if slot_index == 0:
                slot_type = SlotType.LARGE
            elif slot_index in (1, 2):
                slot_type = SlotType.MEDIUM
            else:
                slot_type = SlotType.SMALL
            slot_class = SlotResolver.get_obj(slot_type=slot_type)
            slot_obj = slot_class(id=slot_index, type=slot_type, is_occupied=False).create()

            if not slot_map.get(slot_type):
                slot_map[slot_type] = []
            slot_map[slot_type].append(slot_obj)

        floor_obj = Floor(id=floor_index, slot_map=slot_map)
        return floor_obj
