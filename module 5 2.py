class House:
    def __init__(self, name, numberoffloors):
        self.name = name
        self.numberoffloors = numberoffloors

    def go_to(self, newfloor):
        if 1 <= newfloor <= self.numberoffloors:
            for floor in range(1, newfloor + 1):
                print(floor)
        else:
            print("Такого этажа не существует")

    def __len__(self):
        return self.numberoffloors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.numberoffloors}"

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))
