# @author Carey Nation
# @title Chapter 2, Exercise 10
# @description Scale a cookie recipe


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

SUGAR = 1.5
BUTTER = 1
FLOUR = 2.75
SIZE = 48

num_cookies = read_it("How many cookies would you like to cook: ")
factor = num_cookies / SIZE
sugar = SUGAR * factor
flour = FLOUR * factor
butter = BUTTER * factor

print("\nTo cook %d cookies, you will need:" % num_cookies)
print("   %.2fC of Sugar" % sugar)
print("   %.2fC of Flour" % flour)
print("   %.2fC of Butter" % butter)