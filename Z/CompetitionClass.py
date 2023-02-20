class Competition:
    def __init__(self, name, location, date):
        self.name = name
        self.location = location
        self.date = date

    def get_name(self):
        return self.name

    def get_location(self):
        return self.location

    def get_date(self):
        return self.date

    def get_full_description(self):
        return f"{self.name} { self.location} held on {self.date}"

