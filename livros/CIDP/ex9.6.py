class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        print(self.name)
        print(self.type)
    
    def open_restaurant(self):
        print('ta aberto garai')

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):

        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def sabores(self):
        for sabores in self.flavors:
            print(sabores)


restaurant = Restaurant
c = restaurant('marcos', 'comida')
restaurant.describe_restaurant(c)
ice_cream_stand = IceCreamStand('Sorveteria', 'Sorvetes', ['Chocolate', 'Morango', 'Baunilha'])
ice_cream_stand.describe_restaurant()
ice_cream_stand.sabores()