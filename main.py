from services.parking_manager import ParkingManager

if __name__ == '__main__':
    pm = ParkingManager()

    while True:
        input_str = input()
        words = input_str.split()
        if len(words) == 0:
            print("Invalid Command. try Again!")
            continue

        command = words[0]

        if command == "create_parking_lot":
            id, no_of_floors, no_of_slots = words[1], int(words[2]), int(words[3])
            pm.create_parking_lot(id=id, no_of_floors=no_of_floors, no_of_slots=no_of_slots)
            print("Created parking lot with ", no_of_floors, " floors and ", no_of_slots, "slots per floor")

        elif command == "park_vehicle":
            type, regno, color = words[1].lower(), words[2], words[3]
            try:
                ticket = pm.park_vehicle(type=type, regno=regno, color=color)
                print("Parked vehicle. Ticket ID: ", ticket.id)
            except Exception as e:
                print(str(e))

        elif command == "unpark_vehicle":
            ticket_id = words[1]
            ticket = pm.un_park_vehicle(ticket_id=ticket_id)
            vehicle = ticket.vehicle
            print("Unparked vehicle with Registration Number: ", vehicle.regno, " and Color: ", vehicle.color)

        elif command == "display":
            display_type, vehicle_type = words[1], words[2].lower()
            if display_type == "free_count":
                pm.display_count(display_occupied=False, vehicle_type=vehicle_type)
            elif display_type == "free_slots":
                pm.display_slots(display_occupied=False, vehicle_type=vehicle_type)
            elif display_type == "occupied_slots":
                pm.display_slots(display_occupied=True, vehicle_type=vehicle_type)

        elif command == "exit":
            print("Thank You")
            break

        else:
            print("Invalid Command. try Again!")
        print()
# Todo: Add command for displays
