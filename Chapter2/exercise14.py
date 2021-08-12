# @author Carey Nation
# @title Chapter 2, Exercise 14
# @description Calculate compound interest


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


def interest(p, n, t, r):
    exp = n * t

    return p * (1 + r/n) ** exp


principal = read_it("Enter your initial principal: ")
num_compounds = read_it("Enter the number of times interest will compound per year: ")
years = read_it("Enter the number of years: ")
rate = read_it("Enter your interest rate: ")
rate /= 100.0

total = interest(principal, num_compounds, years, rate)

print("Your will have %.2f after this compounding takes place" % total)
