import random
from acme import Product

# Useful to use with random.sample or random.choice to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

def generate_products(num_products=30):
    products = []
    for _ in range(num_products):
        name = f"{random.choice(ADJECTIVES)} {random.choice(NOUNS)}"
        price = random.randint(5, 100)
        weight = random.randint(5, 100)
        flammability = random.uniform(0.0, 2.5)
        prod = Product(name, price, weight, flammability)
        products.append(prod)
    return products

def inventory_report(products):
    names = [p.name for p in products]
    unique_names = len(set(names))
    
    total_price = sum([p.price for p in products])
    total_weight = sum([p.weight for p in products])
    total_flammability = sum([p.flammability for p in products])
    
    avg_price = total_price / len(products)
    avg_weight = total_weight / len(products)
    avg_flammability = total_flammability / len(products)
    
    return (unique_names, avg_price, avg_weight, avg_flammability)

if __name__ == '__main__':
    products = generate_products()
    report = inventory_report(products)
    print(report)