from src.infrastructure import switchlang as switch
import src.program_hosts as hosts
import datetime


def main():
    run()


def run():
    print('****************Welcome customer****************')
    print()
    show_user_options()
    # PyCharm note: DO NOT comment inline
    while True:
        action = hosts.get_action()

        with switch(action) as obj:
            obj.case('C', hosts.create_account)
            obj.case('L', hosts.log_into_account)

            obj.case('O', order_your_item)
            obj.case('V', view_your_order)
            obj.case('M', lambda: 'change_status')
            obj.case(['X','exit','exit()','Get me out'], hosts.exit_app)
            obj.case('?', show_user_options)

            obj.default(hosts.unknown_command)


def show_user_options():
    print('Press the letter in [ ] to indicate your selection')
    print('[C] to Create new account')
    print('[L] to Log into existing account')
    print('[O] to Order your item(s)')
    print('[V] to View your order(s)')
    print('[M] to return to Main Menu')
    print('[X] to exit this app')
    print()


def order_your_item():


def view_your_order():

