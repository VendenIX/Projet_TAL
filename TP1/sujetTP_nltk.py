from nltk.book import *
from nltk.corpus import gutenberg
from nltk.probability import FreqDist

print("**************************")
# 9 textes sous la forme d'une liste de mots/signes mais dont le type est spécial : Text.
# Casting en list pour l'afficher.
print(text1)
print(type(text1))
# print(text1.tokens)

print("**************************")
# pour le reste on les manipule comme une liste de mots/signes
print(text1[20:31])
print(text1[-3])

print("**************************")
# on peut trouver la position de la première occurrence d'un mot
# remarquons la notation pointée
print(text1.index("monstrous"))

print("**************************")
# ou le nombre de mots
print(len(text1))

print("**************************")
# et le nombre de mots différents
print(len(set(text1)))
# on notera la première fonction spécifique au type Text qui produit une FreqDist
print(len(text1.vocab()))
# attention le vocabulaire est sensible à la casse de caractère.

print("**************************")
# le nombre d'occurrence d'une lettre ou d'un mot peut facilement se compter
print(sum(mot.count('o') for mot in text1))
print(text1.count("monstrous"))

print("**************************")
# le pourcentage d'apparition des mots lol et bonjour dans le text 5
print(100*text5.count("lol")/len(text5))
print(100*text5.count("bonjour")/len(text5))

print("**************************")
# la répartition de mots dans un texte
text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])

print("**************************")
# concordance(mot) renvoie chaque occurrence avec son contexte dans une certaine fenêtre
text1.concordance("monstrous", 50, 3)
text2.concordance("affection", 50, 3)
text5.concordance("lol", 50, 3)

print("**************************")
# similar(mot) est un comparateur de concordancier qui donne les mots qui ont un contexte commun avec le mot
text1.similar("monstrous")
text2.similar("monstrous")

print("**************************")
# common_contexts(listeMots) est un comparateur de concordancier qui donne les contextes communs
# à tous les mots de listeMots
text2.common_contexts(["monstrous", "very"])

print("**************************")
# mais il y a d'autres textes , par exemple dans le corpus gutenberg
# Ces textes sont aussi déjà tokenisés de différentes manières
for text in gutenberg.fileids():
    print("\n***************", text, "***************")
    print(gutenberg.raw(text)[-50:].strip())
    print(gutenberg.paras(text))
    print(gutenberg.sents(text))
    print(gutenberg.words(text))


# Il est donc possible d'avoir également un objet de type FreqDist
words_moby = gutenberg.words('melville-moby_dick.txt')
f_dist_moby = FreqDist(words_moby)

# accompagné de ses fonctions
print(f_dist_moby.B())
print(f_dist_moby.N())
print(f_dist_moby.r_Nr())
print(f_dist_moby.Nr(1))
# print(len(f_dist_moby.hapaxes()))
# print(sorted(f_dist_moby.elements()))
print(f_dist_moby.freq('by'))
print(f_dist_moby.get('by', 0))
# print(sorted(f_dist_moby.items()))
print(f_dist_moby.most_common(5))
f_dist_moby.tabulate(5, cumulative=True)
f_dist_moby.plot(70, title="Moby Dick Stats", cumulative=True, percents=True)

# La liste de mots permet également une transformation dans un type compatible avec Nltk
nltk_text_moby = Text(words_moby)
# et donc l'utilisation de toutes les méthodes de Text
# en particulier une autre manière d'avoir le FreqDist
print(nltk_text_moby.vocab())
