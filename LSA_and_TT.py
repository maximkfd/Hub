import numpy as np
from lemma import prepare_text


def get_lsa_frequency_map(prepared_text, kS):
    # получение лемматизированного текста
    # сбор общего словаря
    dictionary = set()
    # добавляем в множество слов все новые слова путем объединения уже имеющегося с множеством слов одного абзаца
    for paragraph in prepared_text:
        dictionary = set.union(dictionary, set(paragraph))

    # создание частотной матрицы вхождения слов (для последующего использования в SVD)
    dictionary_array = list(dictionary)
    frequency_matrix = []

    for i in range(0, len(dictionary_array)):
        my_word = dictionary_array[i]
        frequency_array_for_this_word = []
        for paragraph in prepared_text:
            frequency_array_for_this_word += [paragraph.count(my_word)]
        frequency_matrix += [frequency_array_for_this_word]
    # частотник готов

    # SVD
    U, s, V = np.linalg.svd(frequency_matrix, full_matrices=False)

    S = np.diag(s)
    for i in range(kS, len(s)):
        S[i][i] = 0

    frequency_matrix_recovered = np.dot(U, np.dot(S, V))

    return dictionary, frequency_matrix_recovered


def get_lsa_and_tt_borders(filename, r, kS):
    # перегнали в массив частотников по абзацам
    dictionary_array, all_frequency_map = get_lsa_frequency_map(filename, kS)
    frequency_array_of_maps = []
    for i in range(0, len(all_frequency_map[0])):
        frequency_array_of_maps += [{}]

    for i in range(0, len(all_frequency_map) - 1):
        word = dictionary_array[i]
        # print(i)
        for j in range(0, len(all_frequency_map[0]) - 1):
            if all_frequency_map[i][j] > 0.00000001:
                frequency_array_of_maps[j][word] = all_frequency_map[i][j]

    # собираем косинусы
    cosine_list = [0]
    for i in range(0, len(frequency_array_of_maps) - 1):
        cosine_mul = 0
        for entry_key in frequency_array_of_maps[i]:
            try:
                val1 = frequency_array_of_maps[i][entry_key]
                val2 = frequency_array_of_maps[i + 1][entry_key]  # value in second array
                cosine_mul += val1 * val2
            except:
                continue
        len1 = 0
        len2 = 0
        for entry_value in frequency_array_of_maps[i].values():
            len1 += entry_value * entry_value
        for entry_value in frequency_array_of_maps[i + 1].values():
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
