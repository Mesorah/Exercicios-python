def make_album(artista=None, album=None, musicas=None):
    while True:
        artista = input('artista')
        if artista == 'q':
            break
        album = input('album')
        if  album == 'q':
            break
        musicas = input('música')
        if musicas == 'q':
            break
        print('(digite q para parar)')
        return artista, album, musicas

print(make_album())
print(make_album())