from constants import VehicleType, SlotType
from models.slot import Slot
from services.slot.base import SlotBaseService


class SmallSlotService(SlotBaseService):
    def create_obj(self):
        return Slot(id=self.id, type=SlotType.SMALL, is_occupied=False)