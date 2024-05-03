class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    login_attemts = 0
    
    def describe_user(self):
        print(self.first_name, self.last_name)
    
    def greet_user(self):
        print(f'salve {self.first_name} {self.last_name}')

    def increment_login_attemps(self):
        self.login_attemts += 1
        return self.login_attemts

    def reset_login_attempts(self):
        self.login_attemts = 0
        return self.login_attemts

user = User('Gabriel', 'Rodrigues')
user.describe_user()
user.greet_user()
for c in range(1,6):
    print(user.increment_login_attemps())
    
print(user.reset_login_attempts())