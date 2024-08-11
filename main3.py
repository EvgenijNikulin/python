empty_list = []
print(len(empty_list))

my_fruits = ['apple', 'banana', 'lime']
print(len(my_fruits))

post_ids = [151, 45, 567, 334]
print(len(post_ids))

user_inputs = [True, 'hi', 234, 10.5, "hello world"]
print(len(user_inputs))

print(post_ids[0])
print(post_ids[-1])

post_ids[0] = 555
post_ids[2] = 2345
print(post_ids)

del user_inputs[2]
print(len(user_inputs))
print(user_inputs)


users = [
    {
        'user_id': 134,
        'user_name': 'Alice'
    },
    {
        'user_id': 831,
        'user_name': 'Bob'
    }
]
print(len(users))
print(users[1]['user_name'])

happy_smiles = []
happy_smiles.append('1')
happy_smiles.append('2')
happy_smiles.append('3')
happy_smiles.append('4')
print(happy_smiles)
print(len(happy_smiles))

inputs = [True, 'hi!', 56, 345]
inputs.pop()
print(inputs)
inputs.pop(0)
print(inputs)
removed_element = inputs.pop()
print(removed_element)
print(inputs)

post_ids = [245, 151, 762, 167]
post_ids.sort()
print(post_ids)
post_ids.sort(reverse=True)
print(post_ids)

greeting = "Hello from Python"
greeting_letters = list(greeting)
print(greeting_letters)

my_dict = {'a': 23, 'b': True}
my_dict_key = list(my_dict)
print(my_dict_key)

ratings = [5.0, 2.5, 4.3, 3.7]
print(min(ratings))
print(max(ratings))
print(sum(ratings))
print(sum(ratings)/len(ratings))

my_ratings = [2.5, 5.0]
other_ratings = [3.7, 4.5, 4.9]
all_ratings = my_fruits + other_ratings
print(all_ratings)

ratings = [2.5, 5.0, 4.3, 3.7, 4.5]
first_two_ratings = ratings[:2]
print(first_two_ratings)

midle_ratings = ratings[1:-1]
print(midle_ratings)

last_two_ratings = ratings[-2:]
print(last_two_ratings)

my_cars = ['Mersedes', 'BMW']
# copied_cars = my_cars[:]
# copied_cars = my_cars.copy()
copied_cars = list(my_cars)
copied_cars.append('Audi')
print(copied_cars)
print(my_cars)
print(id(my_cars) == id(copied_cars))

my_nums = [10, 50, 0, 5, 5, 100]
res = my_nums.count(5)
print(res)
my_nums.append(25)
print(my_nums)
my_nums.insert(2, -5)
print(my_nums)
my_nums.extend('abc')
print(my_nums)
other_nums = my_nums.copy()
my_nums.append(3)
other_nums.clear()
print(id(my_nums))
print(id(other_nums))
print(my_nums, other_nums)
print(len(my_nums))

my_spisok = [2, True, -67, 'abs', 980]

del my_spisok[2]
my_spisok2 = [98, 'win']
my_spisok = my_spisok + my_spisok2
print(my_spisok)
