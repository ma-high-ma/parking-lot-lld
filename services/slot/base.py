class SlotBaseService:
    def __init__(self, id, type, is_occupied):
        self.id = id
        self.type = type
        self.is_occupied = is_occupied

    def validate(self):
        pass

    def create_obj(self):
        pass

    def create(self):
        self.validate()
        return self.create_obj()