from Z.Meeting import Meeting


class Competition(Meeting):
    def __init__(self, name, location, date):
        super().__init__(name, location)
        self.date = date

    def get_full_description(self):
        return f"{self.name} { self.location} held on {self.date}"

