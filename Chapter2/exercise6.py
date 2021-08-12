# @author Carey Nation
# @title Chapter 2, Exercise 6
# @description Calculate county and state sales tax for a sale


STATE_SALES_TAX_RATE = 0.05
COUNTY_SALES_TAX_RATE = 0.025


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


sales_amount = read_it("Please enter your sale amount: ")
county_tax = sales_amount * COUNTY_SALES_TAX_RATE
state_tax = sales_amount * STATE_SALES_TAX_RATE
total_tax = county_tax + state_tax
total_due = sales_amount + county_tax + state_tax

print("\nSales amount:     %.2f" % sales_amount)
print("County sales tax:   %.2f" % county_tax)
print("State sales tax:    %.2f" % state_tax)
print("Total sales tax:    %.2f" % total_tax)
print("Total amount due: %.2f" % total_due)
