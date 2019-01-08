
def PowTwoGen(max = 0):
    n = 0
    while n < max:
        yield 2 ** n
        n += 1
    
print(list(PowTwoGen(3)))

# Yield in generators pause the function, saving all states 
# Yield keeps track of the value of local varaibles and states between successive calls

# Printing out a generator function produces a generator object
# Use list() to list out all of the elements/results in the form of an array