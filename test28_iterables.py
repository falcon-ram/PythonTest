nums = [1, 2, 3]

# i_nums = nums.__iter__() # this cause i_nums to become an iterator
i_nums = iter(nums) # this is the same as the above statement

#for num in nums: # num is an iterator, nums is iterable
#    print(num)

#print(dir(nums))
#print(next(nums)) # error nums is not an iterator cause it does not have the next method

print(i_nums)
print(dir(i_nums))

print(next(i_nums)) # iterator has a next method same as the list
print(next(i_nums)) # iterator remembers where it is in the iterable
print(next(i_nums))
#print(next(i_nums)) # this causes an error because the end of the iterable has been reached

# The for loop above is actually doing this
i_nums = iter(nums)
while True:
    try:
        item = next(i_nums)
        print(item)
    except StopIteration:
        break