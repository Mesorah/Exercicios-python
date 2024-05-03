def build_profile(first, last, **user_info):
    user_info['primeiro_nome'] = first
    user_info['last'] = last
    return user_info

build_profile('Gabriel', 'Rodrigues de Aguiar')