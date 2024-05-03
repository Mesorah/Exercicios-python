palavras = ['opa', 'oi', 'kk']

def show_messages():
    for c in palavras:
        print(c)

show_messages()

def send_messages(msg):
    sent_messages = []
    sent_messages.append(msg)

    print(sent_messages)
    print(palavras)

show_messages()
send_messages('op')


