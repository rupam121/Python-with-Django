
n = int(input())
temp = n
_sum = 0
count = 0
temp_n = n
length = 0
while n > 0:
    rem = n % 10
    # temp = _sum % 10 + rem
    _sum += (rem**3)
    count += 1
    # print(rem)
    n = int(n/10)
# print(_sum)

if _sum == temp:
    print(f"{temp} is arestrng/palindrome ")
else:
    print(f"{temp} is not arestrng/palindrome ")


# num = int(input("Enter a number: "))

# # initialize sum
# sum = 0

# # find the sum of the cube of each digit
# temp = num
# while temp > 0:
#    digit = temp % 10
#    sum += digit ** 3
#    temp //= 10

# # display the result
# if num == sum:
#    print(num, "is an Armstrong number")
# else:
#    print(num, "is not an Armstrong number")
