from Z.Meeting import Meeting


class Initiatives(Meeting):
    def __init__(self, name, description, day, hour, location):
        super().__init__(name, location)
        self.description = description  # opis inicjatywy
        self.hour = hour  # godzina inicjatywy
        self.day = day

    def get_full_description(self):
        return f"{self.name} {self.description} held on {self.day} at {self.hour}"