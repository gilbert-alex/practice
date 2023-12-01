# nested dictionaries

"""
containing_dictionary_name = {
    key: {dictionary},
    key: {dictionary},
    key: {dictionary},
}
"""

# a product dictionary containing four products
products = {
    'RB00111': {'name': 'Ray-Ban', 'price': 112.98, 'models': ['black', 'tortise']},
    'DWC0317': {'name': 'Drone', 'price': 72.95, 'models': ['white', 'black']},
    'MTS0540': {'name': 'T-Shirt', 'price': 2.95, 'models': ['sm', 'md', 'lg']},
    'ECD2989': {'name': 'Echo', 'price': 29.99, 'models': []},
}

# print header
print()
print(f"{'ID':<6} {' Name':<17} {'Price':>8} {' Models'}")
print("-" * 60)

# loop throught each dictionary in the products dictionary
for oneproduct in products.keys():
    # get the id of one product
    id = oneproduct
    # get the name of one product
    name = products[oneproduct]['name']
    # get the unit price of one product & format with $
    unit_price = '$' + f"{products[oneproduct]['price']:,.2f}"
    # create empty string for models
    models = ''
    # loop through the models list and tack onto models
    # one item from the list followed by a comma and a space
    for m in products[oneproduct]['models']:
        models += m + ", "
    # if the models variable is more than two characters in length,
    # peel off the last two characters (floating comma and space)
    if len(models) > 2:
        models = models[:-2]
    else:
        # otherwise, if no models, show none
        models = '<none>'
    # print all the variables with an f string
    print(f'{id:<6} {name:<17} {unit_price:>8} {models}')