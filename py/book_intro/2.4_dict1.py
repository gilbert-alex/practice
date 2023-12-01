# multi key dictionaries

# example 1
employee = {
    'name': 'Haru Tanaka',
    'year_hired': 2005,
    'dob': '11/23/1987',
    'has_laptop': False
}

# example 2
product = {
    'name': "Ray-Ban",
    'unit_price': 112.99,
    'taxable': True,
    'in_stock': 10,
    'models': ['Black', 'Tortise']
}

# display dictionary data by calling the key
print('\nProduct:')
print(product['name'])
print(product['unit_price'])
print(product['taxable'])
print(product['in_stock'])
print(product['models'])

# display dictionary data with f-string
print('\nProduct with f-string:')
print('Name:    ', product['name'])
print('Price:   ', f"${product['unit_price']:.2f}")
print('Taxable: ', product['taxable'])
print('In Stock ', product['in_stock'])
print('Models:')
for model in product['models']:
    print(" " * 10 + model)

# fromkeys()
# create a new dictionary with the same list as a dict which already exists
print('\nCreate a new dict with keys from existing')
DWC001 = dict.fromkeys(product.keys())
print(DWC001)

# setdefault()
# setdefault will not change an existing value (see taxable)
# setdefault will add non-existent keys (see reorder point)
print('\nSet default')
DWC001.setdefault('taxable',True)
DWC001.setdefault('models',[])
DWC001.setdefault('reorder_point',100)
print(DWC001)

print('\nUpdate taxable value')
DWC001['taxable'] = True
print(DWC001)
