class Caneta:
    def __init__(self, cor):
        self.cor = cor
    
    @property
    def cor_tinta(self):
        print('foi')
        return self.cor
    
    @property
    def cor_tampa(self):
        return 123

caneta = Caneta('Azul')
print(caneta.cor_tinta)
print(caneta.cor_tinta)
print(caneta.cor_tinta)
print(caneta.cor_tinta)
print(caneta.cor_tinta)
print(caneta.cor_tampa)













# class Caneta:
#     def __init__(self, cor):
#         self.cor = cor
    
#     def ger_cor(self):
#         print('get cor')
#         return self.cor

# caneta = Caneta('Azul')
# print(caneta.ger_cor())
# print(caneta.ger_cor())
# print(caneta.ger_cor())
# print(caneta.ger_cor())
# print(caneta.ger_cor())