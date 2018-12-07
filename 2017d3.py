from itertools import count
# Advent of Code 2017 day 3
# https://adventofcode.com/2017/day/3

input = 312051

# 1, 9, 25, 49 ... https://en.wikipedia.org/wiki/Centered_octagonal_number

# orbit = (2n-1)^2
# 2n-1^2 = input :: input**.5+1

print (input**.5+1)/2

# n = 279.8076...

print (2*279-1)**2 # 310249
print (2*280-1)**2 # 312481

perim = (2*280-1)**2 - (2*279-1)**2
print perim/4, 558*4

# so, 558-length sides.
print 312481 - 558 < input
# input is on the bottom side
print 312481-input # 430 left of SE corner

print 279*2 # distance from bottom corner
print "#1: {}".format(430-279+279) # 

# cheat for #2: https://oeis.org/A141481


#for n in range(1,1000):
#	print ((2*n-1)**2)
