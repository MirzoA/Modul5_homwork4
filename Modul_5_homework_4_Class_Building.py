class Building:
    total = 0

    def __init__(self):
        # обращаться - через именование класса
        Building.total += 1


buildings = []
buildings_size = 40
while len(buildings) < buildings_size:
    new_building = Building()
    buildings.append(new_building)

print('объектов класса Building =', Building.total)