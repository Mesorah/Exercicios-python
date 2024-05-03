class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, ebom):
        self.name = restaurant_name
        self.type = cuisine_type
        self.ebom = ebom

    def describe_restaurant(self):
        print(self.name)
        print(self.type)
        print(f'é bom garai {self.ebom}')
    
    def open_restaurant(self):
        print('ta aberto garai')

restaurant = Restaurant
c = restaurant('marcos', 'comida', '?')
restaurant.describe_restaurant(c)
restaurant.open_restaurant(c)