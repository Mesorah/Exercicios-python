class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        print(self.name)
        print(self.type)
    
    def open_restaurant(self):
        print('ta aberto garai')

restaurant = Restaurant
c = restaurant('marcos', 'comida')
restaurant.describe_restaurant(c)
restaurant.open_restaurant(c)