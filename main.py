from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
mony_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
while True:
    customer_order = input(f"What would you like? ({menu.get_items()}): ").lower()
    if customer_order == "off":
        break
    elif customer_order == "report":
        coffee_maker.report()
        mony_machine.report()
    else:
        drink = menu.find_drink(customer_order)
        if drink != None:
            if coffee_maker.is_resource_sufficient(drink):
                if mony_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)