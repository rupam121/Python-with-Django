# string = "abba"
# x = len(string)
# print(string[4:x])
# print(string[-5:-1])

# print(string.isupper()) #false
# print(string.upper())
# print(string.capitalize())
# print(string.index("g")) #6
# print(string.isdecimal()) #false
# print(string.replace("d", "O"))  # abcOefgh

# REVERSE string INDEXING ITERATION
string = "MOM"
x = len(string)
rev_str = ""
for i in range(x-1, -1, -1):
    # print(string[i])
    rev_str += string[i]
print(rev_str)
if string == rev_str:
    print(f"[{string} is pallendrom")
else:
    print(f"{string} Not pallendrome")


# CONCATINATION
# s1 = "abcd"
# s2 = "+efgh"
# s3 = s1+s2
# print(s3)
