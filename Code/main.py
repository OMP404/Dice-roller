import pyfiglet
import random

def RollDice(sides):
    pass


def main():
    while True:
        logo = pyfiglet.figlet_format("Dice Roller")
        print(logo)
        print("\n"*5)
        print("1. Roll dice \n ")
        print("2. Statistics \n ")
        print("3. Exit \n ")
        print("\n"*5)

        menu_choice = input("Choose an option: ")
        print("\n"*20)
        if menu_choice == "1":
            print("Choose a die")
            print("""
            1. a Coin (two sided die)
            2. a Cetrahedron (four sided die)
            3. a Common die (six sided die)
            4. a Octahedron (eigth sided die)
            5. a Pentagonal trapezohedron (10 sided die)
            6. a Dodecahedron (12 sided die)
            7. a Icosahedron (20 sided die)
            """)
            print("\n"*17)
            sides = input("Choose the amount of sides on the die: ")
            RollDice(sides)

if __name__ == "__main__":
    main()
