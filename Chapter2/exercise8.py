# @author Carey Nation
# @title Chapter 2, Exercise 8
# @description Calculate tip and tax for a meal

TIP_RATE = 0.18
SALES_TAX_RATE = 0.07


def read_it(prompt):
    # read a single value, makes sure it is a valid number, and return it
    valid = False
    f = 42  # get it scoped out here so the return can find it
    s = 'nothing'

    while not valid:
        try:
            s = input(prompt)
            f = float(s)
            valid = True
        except ValueError:
            print(s + " is not a valid number, please try again")

    return f


sale_amount = read_it("Please enter the cost for your meal: ")
tip_amount = sale_amount * TIP_RATE
sales_tax_amount = sale_amount * SALES_TAX_RATE
total_due = tip_amount + sales_tax_amount + sale_amount

print("\nThe cost of your meal was: %.2f" % sale_amount)
print("The tip amount is:          %.2f" % tip_amount)
print("The sales tax amount is:     %.2f" % sales_tax_amount)
print("The total due is:          %.2f" % total_due)
