# Create your own iterator! Can be infinite, or raise StopIteration under specific conditions

class InfiniteIterator():
    # infinite iterator that returns all odd numbers
    def __iter__(self):
        self.number = 1
        return self

    def __next__(self):
        number = self.number
        self.number += 2
        return number

iterable_object = iter(InfiniteIterator())

print(iterable_object) # Print an object

print("Hello!")
print("Next: ")
print(next(iterable_object))
print("Next: ")
print(next(iterable_object))
print("Next: ")
print(next(iterable_object))


class PowTwo():
    # Gives the next power of 2 in each iteration, up to a certain exponent, n
    def __init__(self, max=0): # takes in one argument, max (default 0)
        self.max = max

    def __iter__(self):
        self.n = 0 # self.n is the number that is being displayed! Must start at 0
        return self

    def __next__(self):
        # if self.n <= self.max - 1: # Either of these work
        if self.n + 1 <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result

        else:
            raise StopIteration

print("PowTwo!")
iterable_object2 = iter(PowTwo(5))

print(next(iterable_object2))
print(next(iterable_object2))
print(next(iterable_object2))
print(next(iterable_object2))
print(next(iterable_object2))
