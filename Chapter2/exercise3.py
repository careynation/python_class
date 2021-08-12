# @author Carey Nation
# @title Chapter 2, Exercise 3
# @description Calculate acreage

sq_ft_per_acre = 43560

sq_ft_s = input("Enter your square feet: ")

try:
    sq_ft = float(sq_ft_s)
    acres = sq_ft / sq_ft_per_acre

    print("You have %.2f acres of land" % acres)
except:
    print(sq_ft_s + " is not a valid number, please try again")