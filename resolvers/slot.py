from constants import VehicleType
from services.slot.bike import BikeSlotService
from services.slot.car import CarSlotService
from services.slot.truck import TruckSlotService


class SlotResolver:
    type_to_slot_mapping = {
        VehicleType.CAR: CarSlotService,
        VehicleType.TRUCK: TruckSlotService,
        VehicleType.BIKE: BikeSlotService,
    }
    @classmethod
    def get_obj(cls, slot_type):
        return cls.type_to_slot_mapping[slot_type]
