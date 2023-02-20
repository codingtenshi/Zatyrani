class Zatyrani:  # zakładam, że obiekt zatyrany ma wymagane imię i skąd jest

    def __init__(self, name, from_where):  # definicja klasy

        self.name = name  # inicjalizacja klasy (podstawowe/standardowe części składowe obiektu)
        self.from_where = from_where
        self.since_when = str
        self.description = str  # opis biegacza
        self.competition = []
        self.initiative = []

    def add_description(self, description):
        self.description = description

    def add_since_when(self, since_when):
        self.since_when = since_when

    def add_competition(self, c):
        self.competition.append(c)

    def list_competition(self):
        for c in self.competition:
            c_desc: str = f'{self.name} ' \
                        f'took parts in {c.get_name()} ' \
                        f'on {c.get_location()} ' \
                        f'in {c.get_date()}'
            print(c_desc)

    def add_initiative(self, i):  # dodałam to po to, aby w obiekcie zatyrany można była dodać inicjatywy
        self.initiative.append(i)

    def list_initiatives(self):
        for i in self.initiative:
            i_desc = f'{self.name} is the organizer of the event' \
                        f' {i.get_name()}' \
                        f' {i.get_description()}' \
                        f' held on {i.get_day()} ' \
                        f'at {i.get_hour()} '
            print(i_desc)

