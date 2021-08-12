# @author Carey Nation
# @title Chapter 2, Exercise 5
# @description Calculate distance traveled


SPEED = 70


def distance(time):
    return time * SPEED


print("Distance in six hours: %.2f miles" % distance(6))
print("Distance in ten hours: %.2f miles" % distance(10))
print("Distance in fifteen hours: %.2f miles" % distance(15))
