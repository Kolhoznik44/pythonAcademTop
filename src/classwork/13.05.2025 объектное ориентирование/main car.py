from car import Sedan
from car import Interface
from car import SUV
from car import Cargo

def drive(obj: Interface):
    obj.start_engine()
    obj.forward_moving()
    obj.backward_moving()

if __name__ == "__main__":
    sed = Sedan(200000, "Чепырка", "салатовый", 1000, "АКПП", 5)
    sed1 = Sedan(1500000, "Копейка", "Белый", 50, "МКПП", 5)
    suv1 = SUV(200000, "Уаз", "черный", 500, True, True, True, "бензин")
    track = Cargo(5000000, "КАМАЗ", "белый", 1000, 12, True, True, 2)

    # print(sed, end='\n\n')
    # print(sed1, end='\n\n')
    # print(suv1, end='\n\n')
    # print(track, end='\n\n')

    cars = [sed, sed1, suv1, track]
    sed2 = Sedan(200000, "тринашка", "салатовый", 1000, "АКПП", 5)
    cars.append(sed2)


    for car in cars:
        print(car)
        drive(car)
        print()


