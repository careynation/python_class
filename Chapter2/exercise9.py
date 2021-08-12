# @author Carey Nation
# @title Chapter 2, Exercise 7
# @description Calculate tip and tax for a meal


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


def convert(c):
    return (9.0 / 5) * c + 32


celsius = read_it("Please enter your temperature, in celsius: ")
fahrenheit = convert(celsius)

print("\n%.2fC is %.2fF" % (celsius, fahrenheit))
