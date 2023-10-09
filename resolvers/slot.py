from constants import VehicleType, SlotType
from services.slot.bike import SmallSlotService
from services.slot.car import LargeSlotService
from services.slot.truck import MediumSlotService


class SlotResolver:
    type_to_slot_mapping = {
        SlotType.LARGE: LargeSlotService,
        SlotType.MEDIUM: MediumSlotService,
        SlotType.SMALL: SmallSlotService,
    }
    @classmethod
    def get_obj(cls, slot_type):
        return cls.type_to_slot_mapping[slot_type]
