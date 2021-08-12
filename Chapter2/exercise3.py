# @author Carey Nation
# @title Chapter 2, Exercise 3
# @description Calculate acreage

SQ_FT_PER_ACRE = 43560

sq_ft_s = input("Enter your square feet: ")

try:
    sq_ft = float(sq_ft_s)
    acres = sq_ft / SQ_FT_PER_ACRE

    print("You have %.2f acres of land" % acres)
except ValueError:
    print(sq_ft_s + " is not a valid number, please try again")