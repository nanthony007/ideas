
import math

cdef str word
word = 'Howdy!'
print(word)

cdef str ans
ans = input('What is your favorite color?')
print(f'My favorite color is blue, but yours is {ans}')


cpdef float avg(list items):
    return math.fsum(items) / len(items)


print(avg([12, 15, 16, 19]))
