divisor = int(input())
bound = int(input())

for number in range(divisor, bound + 1):
    if number % divisor == 0:
        max_multiple = number

print(max_multiple)
