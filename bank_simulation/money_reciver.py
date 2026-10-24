from bank_simulation.money_templates import MONEY_TEMPLATE_FIVE
from bank_simulation.money_templates import MONEY_TEMPLATE_FOUR
from bank_simulation.money_templates import MONEY_TEMPLATE_ONE
from bank_simulation.money_templates import MONEY_TEMPLATE_SEVEN
from bank_simulation.money_templates import MONEY_TEMPLATE_SIX
from bank_simulation.money_templates import MONEY_TEMPLATE_THREE
from bank_simulation.money_templates import MONEY_TEMPLATE_TWO


def recive_money(bank_balance,money_recived=True):

    if money_recived:
        # noinspection PyTypeChecker
        if money_recived==MONEY_TEMPLATE_ONE:
            bank_balance=bank_balance+MONEY_TEMPLATE_ONE
        elif money_recived==MONEY_TEMPLATE_TWO:
            bank_balance=bank_balance+MONEY_TEMPLATE_TWO
        elif money_recived==MONEY_TEMPLATE_THREE:
            bank_balance=bank_balance+MONEY_TEMPLATE_THREE
        elif money_recived==MONEY_TEMPLATE_FOUR:
            bank_balance=bank_balance+MONEY_TEMPLATE_FOUR
        elif money_recived==MONEY_TEMPLATE_FIVE:
            bank_balance=bank_balance+MONEY_TEMPLATE_FIVE
        elif money_recived==MONEY_TEMPLATE_SIX:
            bank_balance=bank_balance+MONEY_TEMPLATE_SIX
        elif money_recived == MONEY_TEMPLATE_SEVEN:
            bank_balance = bank_balance + MONEY_TEMPLATE_SEVEN
        elif money_recived in MONEY_TEMPLATE_ONE and MONEY_TEMPLATE_TWO and MONEY_TEMPLATE_THREE and MONEY_TEMPLATE_FOUR and MONEY_TEMPLATE_FIVE and MONEY_TEMPLATE_SIX and MONEY_TEMPLATE_SEVEN:
            bank_balance= bank_balance+money_recived
recive_money(bank_balance=int)
#<--------------------------------------------------->
