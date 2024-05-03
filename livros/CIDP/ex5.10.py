current_users = ['gabriel', 'joão', 'felipe', 'rodrigo', 'sérgio']
new_users = ['luiz', 'fernando', 'carlos', 'rodrigo', 'felipe']
for c in new_users:
    if c.lower() in current_users:
        print('nome de usário ja utilizado')
    else:
        print('nome de usuário desponível')