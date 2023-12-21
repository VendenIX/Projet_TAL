from sujetTP_tokenizer import *
import wordcloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from collections import Counter


def get_words(tokens):
    return [token.lower() for token in tokens
            if all(car.lower() in "abcdefghijklmnopqrstuvwxyzàâéèêëîïôùûüÿçæœ-'_" for car in token)
            and token.count("'") < 2 and token.count("-") < 4]


def get_stop_words(file_name):
    with open(file_name, 'r', encoding='utf-8') as f_in:
        res = set()
        lines = [line.strip().split(",") for line in f_in.readlines()]
        for line in lines:
            for word in line:
                res.add(word.strip())
        return res


def generate_wordcloud(file_name, max_words=500, stop_words=True, min_len=4, max_len=10, img_mask=None):
    stop_words = get_stop_words("RESOURCES/FR_STOPWORDS.txt") if stop_words else set()
    mask = np.array(Image.open(img_mask)) if img_mask else None
    wc = wordcloud.WordCloud(background_color="white", max_words=max_words, mask=mask)
    tokens = text2Text(file_name).tokens
    f_dist = Counter(token for token in get_words(tokens)
                     if token not in stop_words and min_len <= len(token) <= max_len)
    wc.generate_from_frequencies(f_dist)
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()


if __name__ == "__main__":
    generate_wordcloud("TEXTES/fr_verne.txt")
    generate_wordcloud("TEXTES/fr_verne.txt", img_mask="nlp_mask.png")
    generate_wordcloud("TEXTES/fr_verne.txt", max_words=30, img_mask="nlp_mask.png")
    generate_wordcloud("TEXTES/fr_DH.txt")
    generate_wordcloud("TEXTES/fr_proust.txt")
