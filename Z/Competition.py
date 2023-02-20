class Competition:
    def __init__(self, name, location, date):
        self.name = name
        self.location = location
        self.date = date

    def get_full_description(self):
        return f"{self.name} { self.location} held on {self.date}"

