def metrics(calculated, reference, beta=1.):
    card_inter = 0
    for term in set(calculated):
        card_inter += min(reference.count(term), calculated.count(term))
    if not calculated:
        raise ZeroDivisionError("Can't compute precision : calculated set is empty.")
    if not reference:
        raise ZeroDivisionError("Can't compute recall : reference set is empty.")
    if not card_inter:
        raise ZeroDivisionError("Can't compute F-measure : the intersection of the reference set "
                                "and the calculated set is empty.")
    precision = card_inter / len(calculated)
    recall = card_inter / len(reference)
    f_measure = (1 + beta ** 2) * precision * recall / (beta ** 2 * precision + recall)
    return {"precision": precision, "recall": recall, "F-Measure": f_measure}


txt_fr = """Rapidement, ils ont été fondus avec un alliage de plomb (80%), d'antimoine (5%) et d'étain (15%) dans des
matrices. L'ouvrier typographe se servait d'un composteur sur lequel il alignait les caractères, lus à l'envers, de
gauche à droite, piochés dans une boîte appelée "casse". Les caractères du haut de la casse étaient appelés les
capitales (majuscules) et ceux du bas - les minuscules - les bas-de-casse."""

ref_txt_fr = ['Rapidement', ',', 'ils', 'ont', 'été', 'fondus', 'avec', 'un', 'alliage', 'de', 'plomb', '(', '80', '%',
              ')', ',', 'd\'', 'antimoine', '(', '5', '%', ')', 'et', 'd\'', 'étain', '(', '15', '%', ')', 'dans', 'des',
              'matrices', '.', 'L\'', 'ouvrier', 'typographe', 'se', 'servait', 'd\'', 'un', 'composteur', 'sur',
              'lequel', 'il', 'alignait', 'les', 'caractères', ',', 'lus', 'à', 'l\'', 'envers', ',', 'de', 'gauche',
              'à', 'droite', ',', 'piochés', 'dans', 'une', 'boîte', 'appelée', '"', 'casse', '"', '.', 'Les',
              'caractères', 'du', 'haut', 'de', 'la', 'casse', 'étaient', 'appelés', 'les', 'capitales', '(',
              'majuscules', ')', 'et', 'ceux', 'du', 'bas', '-', 'les', 'minuscules', '-', 'les', 'bas-de-casse', '.']

txt_en = """Monty Python, or The Pythons, is the collective name of the creators of Monty Python's Flying Circus, a
British television comedy sketch show that first aired on the BBC on 5 October 1969. A total of 45 episodes were made
over four series. The Python phenomenon developed from the original television series into something much larger in
scope and impact."""

ref_txt_en = ['Monty', 'Python', ',', 'or', 'The', 'Pythons', ',', 'is', 'the', 'collective', 'name', 'of', 'the',
              'creators', 'of', 'Monty', 'Python', '\'s', 'Flying', 'Circus', ',', 'a', 'British', 'television',
              'comedy', 'sketch', 'show', 'that', 'first', 'aired', 'on', 'the', 'BBC', 'on', '5', 'October', '1969',
              '.', 'A', 'total', 'of', '45', 'episodes', 'were', 'made', 'over', 'four', 'series', '.', 'The', 'Python',
              'phenomenon', 'developed', 'from', 'the', 'original', 'television', 'series', 'into', 'something', 'much',
              'larger', 'in', 'scope', 'and', 'impact', '.']

if __name__ == "__main__":
    cal_text_fr = txt_fr.split()
    cal_text_en = txt_en.split()
    print(metrics(cal_text_fr, ref_txt_fr))
    print(metrics(cal_text_en, ref_txt_en))
