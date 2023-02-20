class Meeting:
    def __init__(self, name, day, location):
        self.name = name
        self.day = day
        self.location = location

    def get_name(self):
        return self.name

    def get_day(self):
        return self.day

    def get_location(self):
        return self.location
