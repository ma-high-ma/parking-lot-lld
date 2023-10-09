class VehicleType:
    CAR = "car"
    BIKE = "bike"
    TRUCK = "truck"

class SlotType:
    LARGE = "large"
    MEDIUM = "medium"
    SMALL = "small"


vehicle_to_slot_mapping = {
    VehicleType.TRUCK: SlotType.LARGE,
    VehicleType.CAR: SlotType.MEDIUM,
    VehicleType.BIKE: SlotType.SMALL
}