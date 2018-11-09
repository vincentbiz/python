def collatz(number):
    if number % 2 == 0:
        result = number / 2
        print(str(result))
        return result
    else:
        result = number * 3 + 1
        print(str(result))
        return result

print("enter a number to be collatzed")
try:
    num = int(input())
    while num != 1:
        num = collatz(num)
except ValueError:
    print('please provide an integer')
