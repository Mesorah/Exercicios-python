class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type

    number_served = 0

    def describe_restaurant(self):
        print(self.name)
        print(self.type)
    
    def open_restaurant(self):
        print('ta aberto garai')
    
    def set_number_served(self, new_number):
        self.number_served = new_number
        return self.number_served
    
    def increment_number_served(self, novos_numeros):
        self.number_served += novos_numeros
        return self.number_served
    

restaurant = Restaurant
c = restaurant('marcos', 'comida')
restaurant.describe_restaurant(c)
restaurant.open_restaurant(c)
client = Restaurant.number_served
print(client)
client += 1
print(client)
print(c.set_number_served(45))
print(c.increment_number_served(100))