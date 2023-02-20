from MeetingClass import Meeting


class Initiatives(Meeting):
    def __init__(self, name, description, day, hour, location):
        super().__init__(name, day, location)
        self.description = description  # opis inicjatywy
        self.hour = hour  # godzina inicjatywy

    def get_description(self):
        return self.description

    def get_hour(self):
        return self.hour

    def initiative_full_description(self):
        return f"{self.name} {self.description} held on {self.day} at {self.hour}"