n = input("Write a number: \n")
def countDigits(n):
    digitcount = 0
    sum = 0
    for x in n:
        if x.isdigit():
            digitcount+=1
            sum = sum + int(x)
    return digitcount, sum

digitcount, sum = countDigits(n)

print("Sum", sum)
print("Count", digitcount)