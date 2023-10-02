from services.parking_lot import ParkingLotService
from services.ticket import TicketService
from services.vehicle import VehicleService


class ParkingManager:
    parkingLotMap = {}
    ticketMap = {}

    # todo add floor to parking lot command

    def create_parking_lot(self, id, no_of_floors, no_of_slots):
        parking_lot = ParkingLotService().create(id=id, no_of_floors=no_of_floors, no_of_slots=no_of_slots)
        self.parkingLotMap[parking_lot.id] = parking_lot

    def get_available_slot(self, parking_lot_id, type):
        parking_lot = self.parkingLotMap[parking_lot_id]
        for floor in parking_lot.floors:
            for slot in floor.slots:
                if not slot.is_occupied and slot.type == type:
                    return slot
        return None

    def create_ticket(self, vehicle, parking_lot_id, slot):
        ticket = TicketService().create(parking_lot_id=parking_lot_id, slot=slot, vehicle=vehicle)
        self.ticketMap[ticket.id] = ticket
        return ticket

    def park_vehicle(self, type, regno, color, parking_lot_id="PR1234"):
        vehicle = VehicleService().create(type=type, regno=regno, color=color)
        slot = self.get_available_slot(parking_lot_id, type)
        if not slot:
            # Todo raise exception
            print("No slot left")
            return
        slot.is_occupied = True
        return self.create_ticket(vehicle=vehicle, parking_lot_id=parking_lot_id, slot=slot)

    def un_park_vehicle(self, ticket_id):
        ticket = self.ticketMap[ticket_id]
        slot = ticket.slot
        slot.is_occupied = False
        return ticket

    def display_count(self, display_occupied, vehicle_type, parking_lot_id="PR1234"):
        parking_lot = self.parkingLotMap[parking_lot_id]
        for floor in parking_lot.floors:
            count = 0
            for slot in floor.slots:
                if slot.type == vehicle_type and slot.is_occupied == display_occupied:
                    count += 1
            print("No. of free slots for", vehicle_type, " on Floor ", floor.id, ": ", count)

    def display_slots(self, display_occupied, vehicle_type, parking_lot_id="PR1234"):
        parking_lot = self.parkingLotMap[parking_lot_id]
        for floor in parking_lot.floors:
            slots = ""
            for slot in floor.slots:
                if slot.type == vehicle_type and slot.is_occupied == display_occupied:
                    slots += f"{slot.id} "
            print("Occupied slots for ", vehicle_type, " on Floor ", floor.id, " : ", slots)

