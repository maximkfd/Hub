from LSA_and_TT import get_lsa_frequency_map
# from cluster import lda

from prostoTT import get_tt_borders
from lemma import prepare_text

cosine_border_file = "cb"
singular_numbers_file = "sn"


def set_cosine_border(border):
    file = open("cb", 'w')
    file.write(str(border))
    file.close()


def set_number_of_singular_numbers(n):
    file = open("sn", 'w')
    file.write(str(n))
    file.close()


def text_markup(filename, algorithm):
    cosine_border = float(open(cosine_border_file, 'r').read())
    singular_numbers = int(open(singular_numbers_file, 'r').read())
    return text_markup_with_parameters(filename, algorithm, cosine_border, singular_numbers)


def text_markup_with_parameters(filename, algorithm, cosine_border, singular_numbers):
    lemmatized = prepare_text(filename)
    if algorithm == "Text Tiling":
        return get_tt_borders(lemmatized, cosine_border)
    if algorithm == "LSA + Text Tiling":
        return get_lsa_frequency_map(lemmatized, singular_numbers)
    # if algorithm == "Cauterization":
    #     return lda(lemmatized, )
    return None