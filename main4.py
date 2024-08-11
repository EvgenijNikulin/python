my_motorbike = {
    'brand': 'Ducati',
    'price': 25000,
    'engine_vol': 1.2,
}

other_motorbike = {

    'price': 25000,
    'engine_vol': 1.2,
    'brand': 'Ducati',
}
print(my_motorbike == other_motorbike)
print(id(my_motorbike) == id(other_motorbike))
my_motorbike['price'] = 20000
my_motorbike['is_new'] = True
del my_motorbike['engine_vol']
key_name = 'brand'
my_motorbike[key_name] = 'BMW'
print(my_motorbike)
print(my_motorbike['brand'])
# print(dir(my_motorbike))

my_motorbike = {
    'brand': 'Ducati',
    'engine_vol': 1.2,
    'price_info': {
        'price': 30000,
        'is_available': True
    }}
print(my_motorbike['price_info']['price'])
print(my_motorbike['price_info']['is_available'])

brand = 'Java'
bike_price = 2_000_000
engine_volume = 1.2
my_motorbike = {
    'brand': brand,
    'price': bike_price,
    'engine_vol': engine_volume,
}
print(my_motorbike)
print(len(my_motorbike))
# del my_motorbike['price']
print(len(my_motorbike))
print(my_motorbike.get('qty', 0))
print(my_motorbike.get('brand'))
print(my_motorbike.get('price'))

my_dict = {}
# print(my_dict.__doc__)
my_disk = {}
print(id(my_disk))
print(type(my_disk))
my_disk['brand'] = 'Samsung'
my_disk['price'] = 180
print(my_disk)
print(id(my_disk))
print(my_disk.items())
print(my_disk.get('type'))
print(my_disk)

new_disk = my_disk.copy()
new_disk['type'] = 'ssd'
print(my_disk)
print(new_disk)
print(len(new_disk))

my_list = [['first', 0], ['second', True]]
my_dict = dict(my_list)
print(my_dict)


# Home work
my_slov = {}
name_key1 = input("Enter name key1: ")
key1 = input("Enter znachenie key1: ")
name_key2 = input("Enter name key2: ")
key2 = input("Enter znachenie key2: ")
name_key3 = input("Enter name key3: ")
key3 = input("Enter znachenie key3: ")
my_slov = {
    name_key1: key1,
    name_key2: key2,
    name_key3: key3,
}
my_slov['color'] = 'blue'
my_slov['avtor'] = 1
del my_slov[name_key2]
print(my_slov)
