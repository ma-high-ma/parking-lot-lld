from constants import VehicleType
from models.slot import Slot
from services.slot.base import SlotBaseService


class BikeSlotService(SlotBaseService):
    def create_obj(self):
        return Slot(id=self.id, floor=self.floor, type=VehicleType.BIKE, is_occupied=False)