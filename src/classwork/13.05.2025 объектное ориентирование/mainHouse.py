from house import House
from house import Basement
from house import Floor
from house import Roof
from house import Buildings
from house import Additional_options
def prices (obj:House):
    obj.cost()


if __name__ == "__main__":
    basement = Basement("Кирпич","Имеются",100,10)
    floor = Floor(1000, 3,3)
    roof = Roof("Жилой", 3," Имеется")
    buildings = Buildings(10000, "Баня, Беседка, Бассейн")
    additional_options = Additional_options()

house = [basement, floor, roof, buildings, additional_options]

for i in house:
    print(i)
    prices(Basement)
    print()