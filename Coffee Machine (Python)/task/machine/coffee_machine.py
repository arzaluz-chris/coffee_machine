class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550

    def process_action(self, action):
        if action == "buy":
            self.buy()
        elif action == "fill":
            self.fill()
        elif action == "take":
            self.take()
        elif action == "remaining":
            self.remaining()

    def buy(self):
        choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
        if choice == "1":
            self.make_coffee(250, 0, 16, 4)  # Espresso
        elif choice == "2":
            self.make_coffee(350, 75, 20, 7)  # Latte
        elif choice == "3":
            self.make_coffee(200, 100, 12, 6)  # Cappuccino

    def make_coffee(self, water_needed, milk_needed, beans_needed, cost):
        if self.water < water_needed:
            print("Sorry, not enough water!")
        elif self.milk < milk_needed:
            print("Sorry, not enough milk!")
        elif self.beans < beans_needed:
            print("Sorry, not enough coffee beans!")
        elif self.cups < 1:
            print("Sorry, not enough disposable cups!")
        else:
            print("I have enough resources, making you a coffee!")
            self.water -= water_needed
            self.milk -= milk_needed
            self.beans -= beans_needed
            self.cups -= 1
            self.money += cost

    def fill(self):
        self.water += int(input("Write how many ml of water you want to add: "))
        self.milk += int(input("Write how many ml of milk you want to add: "))
        self.beans += int(input("Write how many grams of coffee beans you want to add: "))
        self.cups += int(input("Write how many disposable cups you want to add: "))

    def take(self):
        print(f"I gave you ${self.money}")
        self.money = 0

    def remaining(self):
        print(f"""The coffee machine has:
        {self.water} ml of water
        {self.milk} ml of milk
        {self.beans} g of coffee beans
        {self.cups} disposable cups
        ${self.money} of money""")

# Main loop
coffee_machine = CoffeeMachine()
while True:
    user_action = input("Write action (buy, fill, take, remaining, exit): ")
    if user_action == "exit":
        break
    coffee_machine.process_action(user_action)
