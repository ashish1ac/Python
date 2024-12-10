"""
Account Balance shouldn't be less than 5000
Account Balance is 10,000
If person withdraw some amount then you have to tell the left amount in the bank,
and if after withdrawing the amount if account balance is less than 5000 then show exception Account Balance Exception
"""


class MinimumAccountBalanceException(Exception):
    pass


account_balance = 10000


def withdraw(how_much):
    global account_balance

    if account_balance - how_much < 5000:
        raise MinimumAccountBalanceException("You have to maintain a minimum balance of 5000!, that's why denying "
                                             "this request")
    else:
        return "Left Account Balance", account_balance - how_much


try:
    print(withdraw(6000))
except MinimumAccountBalanceException as msg:
    print(msg)
