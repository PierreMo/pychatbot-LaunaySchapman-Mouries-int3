# pychatbot-LaunaySchapman-Mouries-int3
# Launay-Schapman Alexis and Pierre Mouriès

# role of the file: Part II of the project: computation on a question, similarity with texts, finding an "answer"


#### IMPORTATIONS ####
### Modules importations
from modules import text_treatment as tx
from modules import computations as cmp
import math

### Global Variables importation
# importation of IDF matrix from computations.py and associated row index, column index
TF_IDF_MATRIX, WORDS, FILES = cmp.TF_IDF_MATRIX, cmp.WORDS, cmp.FILES
# importation of the associated names (list with duplication)
names = cmp.NAMES
# importation of the IDF dictionnary of the corpus
IDF_corpus = cmp.IDF

#### FUNCTIONS ####

# PART II
# 1
def tokenization(question: str) -> list:
    tx.write_in_file('./modules/question.txt', question)
    lowercase = tx.file_in_lowercase('./modules/question.txt')
    tx.write_in_file('./modules/question.txt', lowercase)
    question_cleaned = tx.file_cleaning('./modules/question.txt')
    return question_cleaned.split()


# 2
def intersection_question_corpus(question_word_list: list) -> set:
    set_question = set(question_word_list)
    set_words = set(WORDS)
    return set_question & set_words


# 3
def TF_IDF_vector_question(question: str) -> list:
    question_word_list = tokenization(question)
    set_question = set(question_word_list)
    # associting a TF to each word
    TF_question_vector = []
    for word in WORDS:
        if word in set_question:
            count = 0
            for e in question_word_list:
                if e == word:
                    count += 1
            TF_question_vector.append(count)
        else:
            TF_question_vector.append(0.0)
    # creating the T-IDF vector of the question
    TF_IDF_question = []
    for i in range(len(TF_question_vector)):
        TF_IDF_question.append(TF_question_vector[i] * IDF_corpus[WORDS[i]])

    return TF_IDF_question


# 4
def scalar_product(A: list, B: list) -> float:
    """
    Take two lists with the same size
    Return a float which is the scalar product of the two lists
    """
    product = 0
    for i in range(len(A)):
        product += A[i] * B[i]
    return product


def vector_norm(A: list) -> float:
    """
    Take a list with the same size
    Return a float which is the scalar product of the two lists
    """
    sume = 0
    for e in A:
        sume += e ** 2
    return math.sqrt(sume)


def similarity_calculating(A: list, B: list) -> float:
    """
    Take two lists(vectors) with the same size
    Return a float which is the similarity score between the two vector/list
    """
    product = scalar_product(A, B)
    normA = vector_norm(A)
    normB = vector_norm(B)
    return product / (normA * normB)


# 5
def index_of_maxi(L: list) -> int:
    max_ind = 0
    for i in range(1, len(L)):
        if L[i] > L[max_ind]:
            max_ind = i
    return max_ind


def most_revelant(question_vector: list) -> str:
    """
    Take the TF-IDF list of a question as parameter (size = number of words in the corpus)
    Return the name of the output file which is the most revelant
    """
    similarity_table = []
    for j in range(len(FILES)):
        text_vector = []
        for i in range(len(WORDS)):
            text_vector.append(TF_IDF_MATRIX[i][j])
        similarity_table.append(similarity_calculating(text_vector, question_vector))

    max_ind = index_of_maxi(similarity_table)

    return FILES[max_ind]


# 6
def I_CAN_ANSWER_WHAT_YOU_WANT(question: str):
    """
    :param question: question to answer
    :return: the answer to the question
    """
    question_tf_idf = TF_IDF_vector_question(question)
    text_target = most_revelant(question_tf_idf)
    highest_tf_idf = index_of_maxi(question_tf_idf)
    word_target = WORDS[highest_tf_idf]

    with open('./speeches/' + text_target, 'r') as f:
        full_text = f.readlines()

    i = 0
    while i < len(full_text) and word_target not in full_text[i]:
        i += 1

    if i == len(full_text):
        return "Sorry, I didn't understand"
    return full_text[i]


def refine_answer(question: str) -> str:
    """
    :param question: a question to answer
    :return: an answer from the text with a litle polite formula at the beginning
    """
    answer = I_CAN_ANSWER_WHAT_YOU_WANT(question)
    if"Comment" in question or "Pourquoi" in question or "Quel" in question or "Quels" in question or "Quelle" in question or "Quelles" in question or "Qui" in question or "Quand" in question or "Où" in question:
        if 64 > ord(answer[0]) > 91:
            answer = chr(ord(answer[0]) + 32) + answer[1:]

        if "Comment" in question:
            result = "Après analyse, " + answer
        elif "Pourquoi" in question:
            result = "Car, " + answer
        elif "Quel" in question or "Quels" in question or "Quelle" in question or "Quelles" in question:
            result = "Selon mes recherches," + answer
        elif "Qui" in question:
            result = "C'est " + answer
        elif "Quand" in question:
            result = "Suite à l'analyse de document historique,  " + answer
        elif "Où" in question:
            result = "Lors de " + answer
    else:
        if 123 > ord(answer[0]) > 96:
            answer = chr(ord(answer[0]) - 32) + answer[1:]

        if "Peux-tu" in question:
            result = "Oui, bien sûr!" + answer
        else:
            result = answer

    with open('./modules/historic.txt', 'a') as f:
        f.write('QUESTION: ' + question + '\n')
    with open('./modules/historic.txt', 'a') as f:
        f.write('ANSWER: ' + result + '\n\n')

    return result


# bonus
def give_historic() -> list:
    """
    Gives historic (every questions and answers are stored in a file)
    """
    try:
        with open('./modules/historic.txt', 'r') as f:
            histo = f.readlines()
    except FileNotFoundError:
        return ["You haven't asked any questions"]
    return histo

def clean_historic():
    with open('./modules/historic.txt', 'w') as f:
        f.write('Historic:')
    return 'Done'
