sandwich_orders = ['x-burguer', 'x-tudo', 'x-salada']
finished_sandwiches = []
tot = len(sandwich_orders)
tott = 0
while tot > 0:
    finished_sandwiches.append(sandwich_orders[tott])
    print(f'seu {sandwich_orders[tott]} está pronto')
    tott += 1
    tot -= 1

toot = 1
for c in finished_sandwiches:
    print(f'{toot}- {c}')

    toot += 1