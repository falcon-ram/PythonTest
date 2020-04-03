# class that behaves like the built in range function

class MyRange:
    def __init__(self, start, end):
        self.value = start
        self.end = end

    # to make a class/object iterable it needs to have the __iter__ method
    # this method has to return an iterator.
    # An iterator is a class/object that has the __next__ method
    def __iter__(self):
        return self

    # We are making this class/object an iterator as well
    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current

nums = MyRange(1, 10)
for num in nums:
    print(num)
print()
nums2 = MyRange(1, 10)
print(next(nums2))
print(next(nums2))
print(next(nums2))
print(next(nums2))
