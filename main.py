from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


is_on = True
maker = CoffeeMaker()
menu = Menu()
money = MoneyMachine()



while is_on:
    choice = input(f"​What would you like? ({menu.get_items()}) :")
    if choice == "off":
        is_on = False
    elif choice == "report":
        maker.report()
        money.report()
    else:
        drink = menu.find_drink(choice)
        if maker.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                maker.make_coffee(drink)