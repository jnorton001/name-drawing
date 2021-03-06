import random

class NameDrawing:
    @staticmethod
    def convertFamilyUnits(familyUnits):
        people = []
        for unit in familyUnits:
            for person in unit:
                exclude = list(unit)
                exclude.remove(person)
                people.append({'name': person, 'exclude': exclude})
        return people
        
    def __init__(self, list):
        self.names = list

    def draw(self):
        if len(self.names) < 2:
            return 'Not enough people in the list!'
        while True:
            restart = False
            results = {}
            giftees = list(self.names)
            for gifter in self.names:
                while True:
                    random_index = random.randint(0, (len(giftees) - 1))
                    possible_giftee = giftees[random_index]
                    if possible_giftee['name'] not in gifter['exclude'] and possible_giftee != gifter:
                        break
                    else:
                        restart = True
                        for remaining_giftee in giftees:
                            if remaining_giftee['name'] not in gifter['exclude'] and remaining_giftee != gifter:
                                restart = False
                        if restart == True:
                            break
                results[gifter['name']] = giftees.pop(random_index)['name']
            if restart == False:
                return results

print "Welcome to the NameDrawer!"
print
print "For each family, type names in this format: Tom, Dick, Harry"
print "When you're finished, just hit return."
print

familyUnits = []
i = 1
while True:
    people = raw_input("Family #"+str(i)+": ")
    if people.lower() == "":
        break
    family = people.split(", ")
    familyUnits.append(family)
    i += 1
print

people = []
for unit in familyUnits:
    for person in unit:
        exclude = list(unit)
        exclude.remove(person)
        people.append({'name': person, 'exclude': exclude})
                
drawing = NameDrawing(people)
results = drawing.draw()
finalResults = []
for i in range(len(results.keys())):
    finalResults.append(results.keys()[i] + " : " + results.values()[i])

for j in finalResults:
    print j
                
