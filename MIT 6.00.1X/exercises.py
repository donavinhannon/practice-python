# Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment
# required by the credit card company each month.

balance = 3329
annualInterestRate = 0.2


def ccBalance(balance, annualIntRate=annualInterestRate, fixedPayment=10, months=1):
    """
    :param balance: positive int or float, current balance owed on credit card
    :param annualInterestRate: positive float, annual interest rate for the credit card
    :param monthlyPaymentRate: positive float, monthly payment rate for the credit card
    :param months: positive int, defaults to 1 and increases by one each function call until 12 is reached
    :return: positive float, rounded to two decimal places, balance on credit card after 1 year of minimum payments
    """
    previousBalance = balance
    monthlyInterestRate = (annualIntRate) / 12.0
    monthlyUnpaidBalance = (previousBalance) - (fixedPayment)
    updatedBalance = (monthlyUnpaidBalance) + (monthlyInterestRate * monthlyUnpaidBalance)
    updatedBalance = round(updatedBalance, 2)
    print(updatedBalance)
    if months == 12:
        if updatedBalance <= 0:
            return 'Lowest Payment: ' + str(fixedPayment) + '\n' + 'Remaining balance: ' + str(updatedBalance)
        else:
            fixedPayment += 10
            return ccBalance(balance, fixedPayment=fixedPayment, months=1)
    else:
        months += 1
        return ccBalance(updatedBalance, fixedPayment=fixedPayment, months=months)


print(ccBalance(balance))
