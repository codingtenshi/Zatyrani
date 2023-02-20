from Z.ZatyraniClass import Zatyrani
from CompetitionClass import Competition
from InitiativesClass import Initiatives


zatyrany = Zatyrani("Lukasz", "Nieborowice")
print(zatyrany.name)
zatyrany.add_description("I like bikes without seats")
print(zatyrany.description)
print(zatyrany.name, "is from", zatyrany.from_where)
zatyrany.add_since_when("since july 2022")
print(zatyrany.name, "started run", zatyrany.since_when)  # na tym kończy się kod

competition1 = Competition("Deep Pits", "14.02.2023", "Nieborowice")
competition2 = Competition("Damrot's Run", "15.03.2023", "Pilchowice")
competition3 = Competition("Extreme Jura", "11.04.2023", "Niegowa")

zatyrany.add_competition(competition1)
zatyrany.add_competition(competition2)
zatyrany.add_competition(competition3)

print(competition1.get_name())  # obiekt i funkcja, która jest w obiekcie
print(competition1.get_full_description())
zatyrany.list_competition()
print('===initiatives===')
initiative1 = Initiatives("Slow running -", "running for everyone", "Tuesday", "7.00 p.m", 'zasupie')
initiative2 = Initiatives("Regular running -", "the fastest rate not for beginners", "Thursday", "7.30 p.m.", 'zasupie')
initiative3 = Initiatives("Nordic Walking -", "meeting for everyone who likes walking with sticks", "Monday", "6.30 p.m", 'zasupie')
initiative4 = Initiatives("Winter swimming -", "body charting", "Sunday", "12.00 a.m", 'zasupie')
initiative5 = Initiatives("Charity relay -", "helping by running", "June", "to determine", 'zasupie')
initiative6 = Initiatives("Training the youngest -", "exercises for children", "Friday", "16.00 p.m.", 'zasupie')
print(initiative1.get_name())
print(initiative1.initiative_full_description())

zatyrany.add_initiative(initiative1)
zatyrany.add_initiative(initiative6)
zatyrany.list_initiatives()

