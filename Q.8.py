numbers = []
for i in range(10):
    num = int(input("Enter an integer: "))
    numbers.append(num)
print("Positive numbers: ", [num for num in numbers if num > 0])
print("Negative numbers: ", [num for num in numbers if num < 0])
print("Odd numbers: ", [num for num in numbers if num % 2 != 0])
print("Even numbers: ", [num for num in numbers if num % 2 == 0])
for num in numbers:
    print(f'{num} occurs {numbers.count(num)} times')
