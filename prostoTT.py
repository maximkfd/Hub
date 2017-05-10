import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy

from lemma import prepare_text


def get_tt_borders(separated_text, r):
    # формирование частотных вхождений слов
    frequency_map = {}
    maps = []
    for i in range(0, len(separated_text)):
        for word in separated_text[i]:
            frequency_map[word] = separated_text[i].count(word)
        maps.append(frequency_map)
        frequency_map = {}

    # подсчет косинусных мер
    cosine_list = [0]
    for i in range(0, len(maps) - 1):
        cosine_mul = 0
        for entry_key in maps[i]:
            try:
                val1 = maps[i][entry_key]
                val2 = maps[i + 1][entry_key]  # value in second array
                cosine_mul += val1 * val2
            except:
                continue
        len1 = 0
        len2 = 0
        for entry_value in maps[i].values():
            len1 += entry_value * entry_value
        for entry_value in maps[i + 1].values():
            len2 += entry_value * entry_value
        cosine_list.append(cosine_mul / (pow(len1, 0.5) * pow(len2, 0.5)))

    # формирование нулей и единиц
    borders = []
    for value in cosine_list:
        if value > r:
            borders.append(0)
        else:
            borders.append(1)

    return borders
