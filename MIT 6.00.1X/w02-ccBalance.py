# Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment
# required by the credit card company each month.

balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04


def ccBalance(balance, annualInterestRate = annualInterestRate, monthlyPaymentRate = monthlyPaymentRate, months = 1):
    """
    :param balance: positive int or float, current balance owed on credit card
    :param annualInterestRate: positive float, annual interest rate for the credit card
    :param monthlyPaymentRate: positive float, monthly payment rate for the credit card
    :param months: positive int, defaults to 1 and increases by one each function call until 12 is reached
    :return: positive float, rounded to two decimal places, balance on credit card after 1 year of minimum payments
    """
    previousBalance = balance
    monthlyInterestRate = (annualInterestRate) / 12.0
    minimumMonthlyPayment = (monthlyPaymentRate) * (previousBalance)
    monthlyUnpaidBalance = (previousBalance) - (minimumMonthlyPayment)
    updatedBalance = (monthlyUnpaidBalance) + (monthlyInterestRate * monthlyUnpaidBalance)
    updatedBalance = round(updatedBalance, 2)
    if months == 12:
        return 'Remaining balance: ' + str(updatedBalance)
    else:
        months += 1
        return ccBalance(updatedBalance, months)


print(ccBalance(balance))