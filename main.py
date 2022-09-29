texte = input('Ecrivez un texte ici et je vous dirai le nombre de mots: ')

(texte.split(' '))

def word_count(texte):
    return (len(texte.split(' ')))

print(word_count(texte))
