mydict = { "apple": 1, "berry": 2, "cherry": 3 }


# keys = mydict.iter()
print("Looping over a dictionary: ")
for key in mydict:
    print(key, mydict[key])

print("")
print("Reverse string generator: ")
def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1,-1,-1):
        yield my_str[i]

# For loop to reverse the string
# Output:
# o
# l
# l
# e
# h
for char in rev_str("hello"):
     print(char)


print("")
print("Reverse string, regular function: ")

def rev_str_reg(my_str):
    length = len(my_str)
    for i in range(length - 1,-1,-1):
        # yield my_str[i]
        print(my_str[i])
    
    return

# print(rev_str_reg("henlo"))

rev_str_reg("Henlo")


print("")
print("Sorting")

a = [3, 6, 8, 2, 78, 1, 23, 45, 9]
reverse_nums = sorted(a, reverse=True)
print(reverse_nums)
print("")


print("Enumerate")

my_list = ["apple", "berry", "cherry"]

for counter, value in enumerate(my_list, 3):
    print(counter, value)

print("Slicing")

my_list = [208, 5, 3, 7, 66, 4]
print(my_list[-1:-4:-2]) # should yield [5, 7]