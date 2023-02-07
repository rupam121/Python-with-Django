n = int(input("Enter n: "))
"""
0 0 => 0 1 => 0 2 => 0 3 => 0 4 =>
1 0 => 1 1 => 1 2 => 1 3 => 1 4 =>
3 0 => 3 1 => 3 2 => 3 3 => 3 4 =>
4 0 => 4 1 => 4 2 => 4 3 => 4 4 =>
"""
# for i in range(n):
#     for j in range(n):
#         print(i, j, end=" => ")
#     print()

""" 
*     * 
  * *
  * *
*     * 
"""
for i in range(n):
    for j in range(n):
        if i == j or i+j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# i = 1
# while i > 0:
#     if i < n:
#         print("*", end=" ")
#     print()
#     i += i

# _sum = 0
# count = 0
# while n > 0:
#     rem = n % 10
#     _sum += rem
#     count += 1
#     print(rem)
#     n = int(n/10)
# print(_sum)
