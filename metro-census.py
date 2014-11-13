#!/bin/python

'''
from : http://opengarden.com/jobs

The 2010 Census puts populations of 26 largest US metro areas at 18897109, 12828837, 9461105, 6371773, 5965343, 5946800, 5582170, 5564635, 5268860, 4552402, 4335391, 4296250, 4224851, 4192887, 3439809, 3279833, 3095313, 2812896, 2783243, 2710489, 2543482, 2356285, 2226009, 2149127, 2142508, and 2134411.

Can you find a subset of these areas where a total of exactly 100,000,000 people live, assuming the census estimates are exactly right? Provide the answer and code or reasoning used. 

'''

areas = ( 18897109, 12828837, 9461105, 6371773, 5965343, 5946800, 5582170, 5564635, 5268860, 4552402, 4335391, 4296250, 4224851, 4192887, 3439809, 3279833, 3095313, 2812896, 2783243, 2710489, 2543482, 2356285, 2226009, 2149127, 2142508,  2134411)

sum = 0
flag = 1
for i in range(0, len(areas)):
    print '#'+str(i) + ':'+ str(areas[i])
    sum += areas[i];
    if (sum > 100000000) and  (flag != 0) :
         print " **** sum : " + str(sum)
         flag = 0

print "total is "  + str(sum)

