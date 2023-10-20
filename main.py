import random as r
import time as t

class Car:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed

    def turnon(self):
        print("Engine is turned on!")

    def turnoff(self):
        print("Engine is turned off!")

    def print_info(self):
        print(f"Car name = {self.name}. Car max speed = {self.max_speed}km per hour.")

race = 1

while race > 0:
    namee = input("What's your car name? - ")
    opnamee = r.choice("Mercedes BMW Volkswagen Lada Ferrari Lamborghini Ford Mustang Mitsubishi Honda Peugeot Lanos".split())

    car = Car(namee, r.randint(160, 360))
    op = Car(opnamee, r.randint(100, 400))

    print("\n")
    car.print_info()
    print("\n")

    wgd1 = input("""What do you want to do?
1 - race
2 - stop the game - """)

    if wgd1 == '2':
        print("Bye!")
        break

    elif wgd1 == '1':
        print(f"Your opponent's car name = {op.name}. Your opponent's car max speed = {op.max_speed}km per hour. Your car max speed = {car.max_speed}km per hour.")
        print("\n")
        car.turnon()
        print("Race is on...")
        print()
        t.sleep(1.5)

        if op.max_speed > car.max_speed:
            print("You lose!")
            car.turnoff()
            print("\n")
            race -= 1
            print(f"Remaining races: {race}")

        elif op.max_speed < car.max_speed:
            print(f"You win!")
            car.turnoff()
            print("\n")
            race += 1
            print(f"Remaining races: {race}")

        else:
            print("Your car's max speed is equal to your opponent's!")

    else:
        print("Something is wrong. Please, try again!")

print("Game over!")