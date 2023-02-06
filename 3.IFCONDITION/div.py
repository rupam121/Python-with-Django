n = int(input("Enter n:"))
if (n % 3 == 0 and n % 5 == 0):
    print("Dvivisible by 3 and 5 .")
elif n % 3 == 0:
    print("Divisible by 3")
elif n % 5 == 0:
    print("Divisible by 5")
else:
    print("N is not divisible by 3 or 5.")
