import nltk  # préchargement de la librairie
#nltk.download() #installation des corpus – à ne pas faire si cela a été déjà fait
from nltk.book import *  # chargement du module book.py (9 textes et 9 phrases)
from nltk.corpus import gutenberg  # importation du corpus de texte ‘gutenberg’

#text1.name
# Parcourir tous les textes 
for text in gutenberg.fileids():
    print(text, gutenberg.raw(text)[:100], "...")
#print("Salut mon pote: ", text1.name)
#print(sent1)
