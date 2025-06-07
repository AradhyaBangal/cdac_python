people = {'Arham': 'Blue', 'Lisa': 'Yellow', 'Vinod': 'Purple', 'Jenny': 'Pink'}

print("Total students:", len(people))

people['Lisa'] = 'Red'

people.pop('Jenny', None)

print("Sorted List of Students and Favourite Colours:")
for name in sorted(people):
    print(name, ":", people[name])