# Project: Bitcoin Calculator
# Author:	     Trevor Flynn
# Date:              07/29/22

"""
|Variables|

I = Investment*
CP = Current Price*
FP = Future Price*
M = Margin*~
S = Shares
ST = Sub-Total
P = Profit
TP = Total Profit
NT = New Total

* indicates these variables are user-dined variables.
~ indicates this variable is optional.

|Variable Assignment|

S = I/CP
ST = S*FP
P = ST-I
TP = P*M
NT = I+TP
"""
#
class ComputePrice:
    def __init__(self, currentPrice=0, investment=0, futurePrice=0, margin=0):
        self.currentPrice = currentPrice
        self.investment = investment
        self.futurePrice = futurePrice
        self.margin = margin

def print_calc():
    shares = calc.investment / calc.currentPrice
    subtotal = shares * calc.futurePrice
    profit = subtotal - calc.investment
    try:  totalProfit = profit * calc.margin
    finally: newTotal = calc.investment + totalProfit
    f'{profit:.2f}'
    f'{totalProfit:.2f}'
    f'{newTotal:.2f}'
    print(f'If you invest ${calc.investment} and the price goes to ${calc.futurePrice}, you will earn ${profit:.2f}, and your marginalized profits are ${totalProfit:.2f}, for a new total of ${newTotal:.2f}')

print("This is a trading calculator to find profits")
calc = ComputePrice(0,0,0,0)
calc.currentPrice = float(input("Please enter the current price of the coin:"))
calc.investment = float(input('Please enter the investment:'))
calc.futurePrice = float(input('Please enter the future price of the coin:'))
user_input = input("Do you need to enter in a margin? yes/no ")
if user_input == 'no':
    print_calc()
else:
    calc.margin = int(input('Please enter in your margin:'))
    print_calc()

