# @author Carey Nation
# @title Chapter 2, Exercise 6
# @description Calculate county and state sales tax for a sale


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


miles = read_it("Please enter number of miles driven: ")
gallons = read_it("Please enter number of gallons of gas used: ")

mpg = miles / gallons

print("\nYour gas mileage is %.2f miles per gallon" % mpg)
