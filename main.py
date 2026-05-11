from abc import ABC, abstractmethod


class Coffee(ABC):

    def __init__(self, name):
        self._name = name
        self._water = 0
        self._milk = 0
        self._coffee = 0

    @abstractmethod
    def recipe(self):
        pass

    @abstractmethod
    def print_art(self):
        pass

    def prepare(self):
        print(f"\nPreparing {self._name}...")
        self.recipe()

        print("\nIngredients:")
        print(f"Water  : {self._water}ml")
        print(f"Milk   : {self._milk}ml")
        print(f"Coffee : {self._coffee}g")

        self.print_art()

        print(f"\n✅ {self._name} is ready!\n")


class Latte(Coffee):

    def __init__(self):
        super().__init__("Latte")

    def recipe(self):
        self._water = 50
        self._milk = 150
        self._coffee = 18

    def print_art(self):
        print(r"""
        ####################
        #                  #
        #      LATTE       #
        #       ☕         #
        #                  #
        ####################
        """)


class Americano(Coffee):

    def __init__(self):
        super().__init__("Americano")

    def recipe(self):
        self._water = 120
        self._milk = 0
        self._coffee = 20

    def print_art(self):
        print(r"""
        ####################
        #                  #
        #    AMERICANO     #
        #       ☕         #
        #                  #
        ####################
        """)


class Matcha(Coffee):

    def __init__(self):
        super().__init__("Matcha")

    def recipe(self):
        self._water = 80
        self._milk = 100
        self._coffee = 0

    def print_art(self):
        print(r"""
        ####################
        #                  #
        #      MATCHA      #
        #       🍵         #
        #                  #
        ####################
        """)


class CoffeeMachine:

    def menu(self):
        while True:

            print("====== COFFEE MACHINE ======")
            print("1. Latte")
            print("2. Americano")
            print("3. Matcha")
            print("4. Exit")

            choice = input("\nSelect your drink: ")

            if choice == "1":
                coffee = Latte()
                coffee.prepare()

            elif choice == "2":
                coffee = Americano()
                coffee.prepare()

            elif choice == "3":
                coffee = Matcha()
                coffee.prepare()

            elif choice == "4":
                print("\nThank you for using Coffee Machine ☕")
                break

            else:
                print("\nInvalid Choice!\n")


if __name__ == "__main__":
    machine = CoffeeMachine()
    machine.menu()