# #print 1-255
#
# for count in range(1,256):
#     print count
#
# #print sum
# total = 0
# for count in range(0,256):
#     total += count
#     print "Sum:",total,
#     print "New number:",count,
#
# #print odd numbers between 1-255
# for number in range (0,256,2):
#     if (number % 2 != 0):
#         print "Number is",number,". This is an odd number"
#
# #interating through the array
# array = [1,3,5,7,9,13]
#
# for i in range(len(array)):
#     print(array)
#
# # Find Max
# # max (a)
# a = [1,3,5,-6,9]
# maximum=0
# for k in a:
#     print '----------', k
#     if k > maximum:
#         maximum = k
#
# print('===========',maximum)
#
# #get average
# myArray = [1, 2, 5, 10, 255, 3]
# sum(myArray) / float(len(myArray))
#
# # Array with odd numbers
# y = []
# for odd_num in range(1,256,2):
#     y.append(odd_num)
# print(y)
#
# # greater than y


#Square the values
oldArray = [1,5,10,-2]
newArray = []
for item in range(len(oldArray)):
    newArray.append(oldArray[item]**2)
    print item
    if (oldArray[item] < 0):
        oldArray[item] = 0
        print(oldArray)
print max(newArray)
print min(newArray)
sum(oldArray) / float(len(oldArray))
print sum(newArray) / float(len(newArray))
for item in range(len(oldArray)-1):
    print(oldArray)

# Eliminate Negative Numbers
# max, min, and average
