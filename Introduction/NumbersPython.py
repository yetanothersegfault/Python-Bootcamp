# Addition is +
addition = 2 + 1
print('2 + 1 = ' + str(addition))

# Subtraction is -
subtraction = 2 - 1
print('2 - 1 = ' + str(subtraction))

# Multiplication is *
multiply = 2 * 2
print('2 * 2 = ' + str(multiply))

# Division is /
division = 3 / 2
print('3 / 2 = ' + str(division))
# Note that a result from division will be a floating point number

# Modulo Operator is %
# Also known as the remainder operator
modulo = 7 % 4
print('The remainder of 7 / 4 is ' + str(modulo))

# Exponents are done with **
exponent = 2 ** 3
print('2 ^ 3 = ' + str(exponent))

# Order of operations exists
order = 2 + 10 * 10 + 3
print('2 + 10 * 10 + 3 = ' + str(order))

# Is different than
order = (2 + 10) * (10 + 3)
print('(2 + 10) * (10 + 3) = ' + str(order))

# We can also use python to tell us what type a variable is by using type()
print(type(order))
print(type(division))
print(type('Hello'))