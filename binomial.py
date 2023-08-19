def factorial(x):
    r = 1
    while x > 0:
        r *= x
        x -= 1
        
    return r

def exponential_number(x, y):
    r = 1
    while y > 0:
      r *= x
      y -= 1
    return r

def binomial(x, y, z):
    r = 0
    i = 0
    while i <= z:
        combination = factorial(z) / (factorial(z - i) * factorial(i))
        first_exponential = exponential_number(x, (z - i))
        second_exponential = exponential_number(y, i)
        r += (combination * first_exponential * second_exponential)
        i += 1
    
    return r

print('Developer - shiva13\n')
print('Binomial - (a + b)^c\n')

while True:
    a = input('a = ')
    b = input('b = ')
    c = input('c = ')
        
    print('Conclusion is {0}\n'.format(binomial(int(a), int(b), int(c))))