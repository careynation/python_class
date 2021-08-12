# @author Carey Nation
# @title Chapter 2, Exercise 13
# @description Calculate the number of vines for a vineyard


def vines(_row_length, _end_space, _vine_spacing):
    return (_row_length - (2 * _end_space)) / _vine_spacing


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


row_length = read_it("Please enter your row length: ")
end_spacing = read_it("Please enter your end space: ")
vine_spacing = read_it("Please enter your vine spacing: ")

total_vines = vines(row_length, end_spacing, vine_spacing)

print("You will need %d total vines per row" % total_vines)
