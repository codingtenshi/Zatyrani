class News:
    def __init__(self, date, description):
        self.date = date
        self.description = description

    def get_date(self):
        return self.date

    def get_description(self):
        return self.description

    def full_description(self):
        return f"{self.description} {self.date}"




