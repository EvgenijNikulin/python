my_comment = "This is my short comment"
print(len(my_comment))
print(my_comment.replace('short', 'long'))
print(my_comment.count('is'))
print(my_comment[0:10])

friends_qty = 50
print(friends_qty)
print(type(friends_qty))

# input_str = input("Enter any namber: ")
# input_int = int(input_str)
# print(input_int)
# print(type(input_int))
# any_num = int(input("Enter any namber: "))

# print(any_num)
# print(type(any_num))

base = 5
power = 3
print(pow(base, power))

one_million = 1_000_000
print(one_million)

my_number = 3_427
print(my_number)

average_price = 17.25
print(average_price)
print(type(average_price))

average_price = 28.75
price = int(average_price)
print(price)
print(type(price))

average_price = 0.85
price = round(average_price)
print(price)
print(type(price))

complex_a = 10 + 7j
complex_b = 3 + 3j
sum = complex_a * complex_b
print(sum)
print(type(sum))

print(100 > 24)
print(-5 > 0)
print('long string' > 'long')
print([1, 2, 3] == [1, 2, 3])

db_is_available = False
print(db_is_available)
print(type(db_is_available))

db_is_available = True
print(db_is_available)

print(bool(10))
print(bool('abc'))
print(bool([]))
print(bool([13, 56]))
print(bool(None))

print(100 > 10)
print('Long string' > 'long')
print([1, 2, 3] == [1, 2, 3])
print({'a': 3} == {'a': 1})

print(int('23') + 7)

int_num = 23
float_num = 5.7
print(float_num.__rmul__(int_num))

bool_val = True
int_val = 8
print(int_val + bool_val)

int_val = 50
str_val = 'abc'
print(str_val * int_val)

print(str.__doc__)

my_list = []
print(help(list.__eq__))
