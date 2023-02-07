# # n = int(input())
# # count = 1
# # for i in range(1, n+1):
# #     count += i
# #     print(count, end=", ")

# # print(count)

# N = int(input())

# a = 0
# b = 1
# sum = 0
# while(sum <= N):
#     print(sum)
#     print()
#     a = b
#     b = sum
#     sum = a + b

N = int(input())
n1, n2 = 0, 1
count = 0
if N == 1:
    print(n1)
else:
    while (count <= N-1):
        print(n1)
        n1 = n2
        n2 = count
        count = n1 + n2
