"""
CP1404 Practical
used cars
"""

from prac_06.car import car

def main():
    my_car = car("My car", 180)
    my_car.drive(30)
    print(f"fuel: {my_car.fuel}")
    print(my_car)
    limo = car("Limo", 100)
    limo.add_fuel(20)
    print(limo.fuel)
    limo.drive(115)
    print(limo)


main()
