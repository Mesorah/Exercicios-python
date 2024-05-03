def make_album(artista, album, musicas=None):
    if musicas:
        pessoa = {'pessoa': artista, 'album': album, 'músicas': musicas}
    else:
        pessoa = {'pessoa': artista, 'album': album}
    return pessoa

print(make_album('Drake', 'Floss', 'Maikon'))
print(make_album('Akon', 'Eminem'))