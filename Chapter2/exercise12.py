# @author Carey Nation
# @title Chapter 2, Exercise 12
# @description Calculate commissions and profit/loss for a stock sale

COMMISSION_RATE = 0.03
SHARES = 2000
BUY_PRICE = 40
SELL_PRICE = 42.75

cost = SHARES * BUY_PRICE
buy_commission = COMMISSION_RATE * cost
total_cost = cost + buy_commission
sell_amount = SHARES * SELL_PRICE
sell_commission = sell_amount * COMMISSION_RATE

profit_or_loss = sell_amount - cost - buy_commission - sell_commission

print("Initial share value: %.2f" % cost)
print("Buy commission %.2f" % buy_commission)
print("Initial transaction cost: %.2f" % (cost + buy_commission))
print("Sell amount: %.2f" % sell_amount)
print("Sell commission: %.2f" % sell_commission)
print("Profit/loss %.2f" % profit_or_loss)

if profit_or_loss > 0:
    print("A profit was made")
else:
    print("A loss was taken")
