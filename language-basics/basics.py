import math
from collections import deque
import heapq

# Dynamically typed: a variable can reference values of different types.
n = 0
print(f"n = {n}")

n = "abc"
print(f"n = {n}")

# Sequence unpacking.
# The number of variables on the left must match the number of values.
n, m = 0, "abc"

# 2 ways to increment, no ++ operator
n = n + 1
n += 1

# None represents the absence of a value (similar to null in other languages).
n = 4
n = None
print(n)

# if / elif / else statements.
# (Python 3.10+ also provides the 'match' statement, similar to switch.)
n = 1
if n > 2:
    n -= 1
elif n == 2:
    n *= 2
else:
    n += 2

# Use "and" instead of "&&", and "or" instead of "||".
n, m = 1, 2
if (n > 2 and n != m) or n == m:
    n += 1

# while loop
while n < 5:
    print(n)
    n += 1

# for loop
for i in range(5):
    print(i)

for i in range(2, 5):
    print(i)

for i in range(5, 1, -1):
    print(i)

# Floating-point division.
print(5 / 2)

# Floor division.
print(5 // 2)

# Prints -2 because // performs floor division (rounds down toward -∞),
# not truncation toward 0.
print(-3 // 2)

# int() truncates toward 0, matching C/C++/Java behavior.
print(int(-3 / 2))

print(10 % 3)

# Returns 2 instead of -1 because Python's // operator performs floor division.
#
# Example:
#   10 / 3  = 3.333...
#   10 // 3 = 3      (floor)
#
# For negative numbers:
#   -10 / 3  = -3.333...
#   -10 // 3 = -4     (floor, not -3)
#
# Since Python guarantees:
#   a == (a // b) * b + (a % b)
#
# We get:
#   -10 = (-4 * 3) + 2
# Therefore, -10 % 3 == 2.
print(-10 % 3)  # 2

# math.fmod() follows the C standard library's definition of remainder.
# It uses truncating division (rounds toward 0), unlike Python's %
# operator, which uses floor division (rounds down).
#
# Example:
#   -10 / 3 = -3.333...
#
#   truncate(-3.333...) = -3   <-- Used by math.fmod()
#   floor(-3.333...)    = -4   <-- Used by Python's // and %
#
# Remainder using truncation:
#   -10 - (-3 * 3)
# = -10 + 9
# = -1
#
# Hence, math.fmod(-10, 3) returns -1.0 (same sign as the dividend).

print(math.fmod(-10, 3))  # -1.0

print(math.floor(3 / 2))
print(math.ceil(3 / 2))
print(math.sqrt(2))
print(math.pow(2, 3))
# math.pow() always returns a float.
# Use ** when you want an integer result for integer operands.

# Python integers have arbitrary precision, so there is no maximum
# or minimum integer value. They can grow as large as available memory allows.
print(2**200)

# Positive and negative infinity are useful as placeholder values
# (e.g., when finding the minimum or maximum in a collection).
# They are not the largest/smallest possible integers.
print(float("inf"))  # inf
print(float("-inf"))  # -inf

arr = [1, 2, 3]
print(arr)

arr.append(4)
arr.append(5)
print(arr)

arr.pop()
print(arr)

arr.insert(1, 7)
print(arr)

arr[0] = 0
arr[3] = 0
print(arr)

n = 5
arr = [1] * n
print(arr)
print(len(arr))

arr = [1, 2, 3]
print(arr[-1])
print(arr[-2])

arr = [1, 2, 3, 4]
print(arr[1:3])
print(arr[0:4])

a, b, c = [1, 2, 3]

nums = [1, 2, 3]
for i in range(len(nums)):
    print(nums[i])

for num in nums:
    # Reassigning 'num' does not modify the original list.
    print(num)

for i, n in enumerate(nums):
    print(i, n)

nums1 = [1, 2, 3]
nums2 = [4, 5, 6]

for n1, n2 in zip(nums1, nums2):
    print(n1, n2)

nums = [1, 2, 3]
nums.reverse()
print(nums)

arr = [5, 3, 7, 3, 8]
arr.sort()
print(arr)

arr.sort(reverse=True)
print(arr)

arr = ["bob", "alice", "jane", "doe"]
arr.sort()
print(arr)

arr.sort(key=lambda x: len(x))
print(arr)
arr.sort(key=len)
print(arr)

arr = [i for i in range(5)]
print(arr)

arr = [i + i for i in range(5)]
print(arr)

# Each row is a separate list object.
# Modifying one row does not affect the others.
arr = [[0] * 4 for _ in range(5)]
print(arr)

# All rows reference the same list object.
# Modifying one row updates every row.
arr = [[0] * 4] * 4
print(arr)

s = "abc"
print(s)
print(s[0:2])
# Strings are immutable.
# s[0] = "A"

print(int("123") + int("123"))
print(str(123) + str(123))

# Unicode code points (ASCII for basic English letters).
print(ord("a"))
print(ord("b"))

strings = ["ab", "cd", "ef"]
print(" ".join(strings))


# deque supports O(1) append/pop operations from both ends.
queue = deque()
queue.append(1)
queue.append(2)
print(queue)

queue.popleft()
print(queue)

queue.appendleft(1)
print(queue)

queue.pop()
print(queue)

# Sets store unique elements.
my_set = set()

my_set.add(1)
my_set.add(2)
print(my_set)
print(len(my_set))

print(1 in my_set)
print(2 in my_set)
print(3 in my_set)

my_set.remove(2)
print(2 in my_set)

print(set([1, 2, 3]))
my_set = {i for i in range(5)}
print(my_set)

my_map = {}
my_map["alice"] = 88
my_map["bob"] = 77
print(my_map)
print(len(my_map))

my_map["alice"] = 80
print(my_map["alice"])
# Membership checks dictionary keys, not values.
print("alice" in my_map)
my_map.pop("alice")
print("alice" in my_map)

my_map = {"alice": 90, "bob": 70}
print(my_map)

my_map = {i: 2 * i for i in range(5)}
print(my_map)

my_map = {"alice": 90, "bob": 70}
print(my_map)

for key in my_map:
    print(key)

for value in my_map.values():
    print(value)

for key, value in my_map.items():
    print(key, value)

tup = (1, 2, 3)
print(tup)
print(tup[0])
print(tup[-1])

# Tuples are immutable (and hashable if their elements are hashable),
# so they can be used as dictionary keys and set elements.
my_map = {(1, 2): 3}
print(my_map[(1, 2)])

my_set = set()
my_set.add((1, 2))
print((1, 2) in my_set)

# cannot use list or other mutable types as keys
# my_map[[3, 4]] = 5

min_heap = []
heapq.heappush(min_heap, 3)
heapq.heappush(min_heap, 2)
heapq.heappush(min_heap, 4)

# min is always at 0 index
print(min_heap[0])

while len(min_heap):
    print(heapq.heappop(min_heap))

# heapq implements a min heap.
# To simulate a max heap for numbers, negate values when pushing and popping.
# For custom objects, implement __lt__() to reverse the comparison.
max_heap = []

heapq.heappush(max_heap, -2)
heapq.heappush(max_heap, -3)
heapq.heappush(max_heap, -4)

# max is always at index 0
print(-1 * max_heap[0])

while len(max_heap):
    print(-1 * heapq.heappop(max_heap))

# build heap from values
arr = [2, 1, 8, 4, 5]
heapq.heapify(arr)
while arr:
    print(heapq.heappop(arr))


def my_func(n, m):
    return n * m


def outer(a, b):
    # Inner functions can access variables from the enclosing function (closure).
    c = "c"

    def inner():
        return a + b + c

    return inner()


print(outer("a", "b"))


def double(arr, val):
    def helper():
        # Mutating the list updates the original object.
        # We are not reassigning 'arr', so no 'nonlocal' is needed.
        for i in range(len(arr)):
            arr[i] *= 2

        # Without 'nonlocal', Python treats 'val' as a new local variable
        # because it is being assigned to. Reading it before that assignment
        # results in:
        # UnboundLocalError: cannot access local variable 'val' where it is
        # not associated with a value.
        #
        # 'nonlocal' tells Python to use the variable from the nearest
        # enclosing function scope instead.
        nonlocal val
        val *= 2

    helper()
    print(arr, val)


nums = [1, 2]
val = 3
double(nums, val)


class MyClass:
    def __init__(self, nums):
        self.nums = nums
        self.size = len(nums)

    def get_length(self):
        return self.size

    def get_double_length(self):
        return 2 * self.get_length()
