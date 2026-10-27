def calcola_media(voti):
    somma = 0
    for voto in voti:
        somma += voto

    media = somma / len(voti)
    return media


def esito(media):
    if media >= 6:
        return "Promosso"
    else:
        return "Non promosso"