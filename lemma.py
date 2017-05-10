from nltk import WordNetLemmatizer
from nltk.corpus import stopwords
from docx import Document


def read_doc(filename):
    print("reading text")
    file = open(filename, 'rb')
    document = Document(file)
    file.close()

    text = []
    for paragraph in document.paragraphs:
        paragraph_text = paragraph.text
        paragraph_text = paragraph_text.lower()
        paragraph_text = paragraph_text.replace(".", "")
        paragraph_text = paragraph_text.replace(",", "")
        paragraph_text = paragraph_text.replace("'", "")
        paragraph_split = paragraph_text.split()
        text.append(paragraph_split)

    return text


def delete_stop_words(text):
    print("deleting words...")
    stop_words = set(stopwords.words('english'))
    text_without_stop = []
    for paragraph in text:
        paragraph_without_stop = [word for word in paragraph if word not in stop_words]
        text_without_stop.append(paragraph_without_stop)
    return text_without_stop


def lemmatize(text):
    lemma_text = []
    wnl = WordNetLemmatizer()
    print("lemmatization...")
    for paragraph in text:
        lemmatized_paragraph = []
        for word in paragraph:
            lemma_word = wnl.lemmatize(word)
            lemmatized_paragraph.append(lemma_word)
        lemma_text.append(lemmatized_paragraph)
    return lemma_text


# Read text, delete stop words, text lemmatization
def prepare_text(filename):
    text_initial = read_doc(filename)
    text_deleted_words = delete_stop_words(text_initial)
    lemmatized_text = lemmatize(text_deleted_words)
    return lemmatized_text



