from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


#created objects 
menu = Menu()
coffee_maker = CoffeeMaker
money_machine = MoneyMachine

coffee_maker.report
money_machine.report

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options})")