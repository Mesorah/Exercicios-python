palavras = ['opa', 'oi', 'kk']

def show_messages():
    for c in palavras:
        print(c)

show_messages()

def send_messages():
    c = palavras.copy()

    print(c)
    print(palavras)

send_messages()