def carros(fa, mo, **dicts):
    dicts['fabricante'] = fa
    dicts['modelo'] = mo
    return dicts


car = carros('subaru', 'outback', color='blue', two_package=True)
print(car)