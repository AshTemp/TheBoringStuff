# for number in range(1,11):
#     if number % 2 > 0:
#         print number

# for number in range (1,11):
#     if number == 5:
#         print "I have counted to %s" % number
#         break

# for number in range(1,11):
#     if number == 5:
#         print "I have counted to %s" % number
#     else:
#         print "I counted from 1 to 10"

# for number in range(1,11):
#     if number == 5:
#         print "I have counted to %s" % number
#         break
#     else:
#         print "I counted from 1 to 10"

# notes = "And a 1 and a 2 and a 3"
# for x in notes:
#     if x.isdigit():
#         print x

import random

# heads_in_a_row_needed = 10
# heads_in_a_row = 0
# total_tries = 0
# while heads_in_a_row_needed != heads_in_a_row:
#     toss = random.randint(0,1)
#     if toss == 1:
#         heads_in_a_row +=1
#     else:
#         heads_in_a_row = 0
#     total_tries +=1
# print "It took %s tries to get %s heads in a row" % (total_tries, heads_in_a_row)

heads_in_a_row_needed = 10
heads_in_a_row = 0
total_tries = 0
while heads_in_a_row_needed != heads_in_a_row:
    toss = random.randint(0, 1)
    if toss == 1:
        heads_in_a_row += 1
    else:
        heads_in_a_row = 0
    total_tries += 1
    if heads_in_a_row_needed == heads_in_a_row:
        break
print("It took %s tries to get %s heads in a row") % (total_tries, heads_in_a_row)
