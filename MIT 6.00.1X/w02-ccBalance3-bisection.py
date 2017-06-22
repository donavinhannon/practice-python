# Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment
# required by the credit card company each month.

balance = 320000
annualInterestRate = 0.2

monthlyInterestRate = (annualInterestRate) / 12.0
lowerBound = (balance / 12)
upperBound = ((balance * (1 + monthlyInterestRate) ** 12) / 12.0)

def calcPayment(lowerLimit, upperLimit):
    return ((lowerLimit + upperLimit) / 2)


def ccBalance(passedInBalance, Payment, months=1, lower=lowerBound, upper=upperBound):
    """
    :param passedInBalance: positive int or float, current balance owed on credit card
    :param Payment: positive float, monthly payment rate for the credit card
    :param months: positive int, defaults to 1 and increases by one each function call until 12 is reached
    lower: positive float, lower limit of payment guesses
    upper: positive float, upper limit of payment guesses

    :return: positive float, rounded to two decimal places, balance on credit card after 1 year of minimum payments
    """
    previousBalance = passedInBalance
    monthlyUnpaidBalance = (previousBalance) - (Payment)
    updatedBalance = (monthlyUnpaidBalance) + (monthlyInterestRate * monthlyUnpaidBalance)
    updatedBalance = updatedBalance

    if months == 12 and -0.001 < updatedBalance < .001:
        return 'Lowest Payment: ' + str(round(Payment, 2))
    elif months < 12:
        months += 1
        return ccBalance(updatedBalance, Payment, months, lower, upper)
    elif months == 12 and updatedBalance > 0:
        lowerlim = Payment
        fixedPayment = calcPayment(lowerlim, upper)
        return ccBalance(balance, fixedPayment, 1, lowerlim, upper)
    elif months == 12 and updatedBalance < 0:
        upperlim = Payment
        fixedPayment = calcPayment(lower, upperlim)
        return ccBalance(balance, fixedPayment, 1, lower, upperlim)


fixedPayment = calcPayment(lowerBound, upperBound)
print(ccBalance(balance, fixedPayment))