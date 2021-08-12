# @author Carey Nation
# @title Chapter 2, Exercise 2
# @description Calculate profit

PROFIT_MARGIN = 0.23

total_sales_s = input("Please enter your total sales: ")

try:
    total_sales = float(total_sales_s)

    profit = total_sales * PROFIT_MARGIN

    print("Your profit is: %2.2f" % profit)
except:
    print(total_sales_s + " is not a valid number, please try again.")