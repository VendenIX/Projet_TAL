import nltk
from sujetTP_tokenizer_naif import *


def tokenizer_fr():
    exceptions = "M\.|aujourd'hui|prud'hom\w+|pommes? de terre"
    nombres = '\d+\.\d+'
    mots = "\w+'?"
    ponctuations = """\.{3}|[\.,;:?!-_«»"]"""
    re_mots = '|'.join([exceptions, nombres, mots, ponctuations])
    return nltk.RegexpTokenizer(re_mots)


def get_tokens(file_name):
    with open(file_name, 'r', encoding='utf-8') as f_in:
        return tokenizer_fr().tokenize(f_in.read())


def text2Text(file_name):
    return nltk.Text(get_tokens(file_name))


if __name__ == "__main__":
    print(metrics(tokenizer_fr().tokenize(txt_fr), ref_txt_fr))
    nltk_text_verne = text2Text("TEXTES/fr_verne.txt")
    f_dist_tokens_verne = nltk_text_verne.vocab()
    f_dist_tokens_verne.plot(100, title="Verne Stats", cumulative=True, percents=True)
    print(f_dist_tokens_verne.most_common(10))
