from models.ticket import Ticket


class TicketService:
    def create(self, parking_lot_id, slot, vehicle):
        id = self.generate_id(parking_lot_id, slot)
        ticket = Ticket(id=id, parking_lot=parking_lot_id, slot=slot, vehicle=vehicle)
        return ticket

    def generate_id(self, parking_lot_id, slot):
        return f"{parking_lot_id}_{slot.id}"