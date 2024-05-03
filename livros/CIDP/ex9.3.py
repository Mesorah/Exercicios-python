class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def describe_user(self):
        print(self.first_name, self.last_name)
    
    def greet_user(self):
        print(f'salve {self.first_name} {self.last_name}')

user = User('Gabriel', 'Rodrigues')
user.describe_user()
user.greet_user()