# @author Carey Nation
# @title Chapter 2, Exercise 4
# @description Calculate sales amount, sales tax, and total cost for five items

# read a single value, makes sure it is a valid number, and return it
def read_it(prompt):
    valid = False
    f = 42  # get it scoped out here so the return can find it

    while not valid:
        try:
            s = input(prompt)
            f = float(s)
            valid = True
        except:
            print(s + " is not a valid number, please try again")

    return f

total_sales = 0

for i in range(5):
    total_sales += read_it("Please enter the price for item %d: " % (1 + i))

sales_tax = 0.07 * total_sales

print("\nSubtotal:  %.2f" % total_sales)
print("Sales tax: %.2f" % sales_tax)
print("Total due: %.2f" % (total_sales + sales_tax))

