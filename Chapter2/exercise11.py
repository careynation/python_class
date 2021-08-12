# @author Carey Nation
# @title Chapter 2, Exercise 11
# @description Calculate percentages of males and females in a class


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


females = read_it("Please enter the number of females in your class: ")
males = read_it("Please enter the number of males in your class: ")
class_size = females + males
female_pct = females / class_size
male_pct = 1.0 - female_pct

print("\nThere are %d total students in your class, of these:" % class_size)
print("%.2fpct(%d) are female" % (100 * female_pct, females))
print("%.2fpct(%d) are male" % (100 * male_pct, males))
