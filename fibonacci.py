import unittest

def fibonacci(number):
    numbers = [0,1]
    total = 1
    for i in range(number):
        total = numbers[i] + numbers[i+1]
        numbers.append(total)
    return total

if __name__== '__main__':
    unittest.main()