import text_treatment as tx
import computations as cmp
import math

# importation of IDF matrix from computations.py and associated row index, column index
TF_IDF_MATRIX, WORDS, FILES = cmp.TF_IDF_MATRIX, cmp.WORDS, cmp.FILES
# importation of the associated names (list with duplication)
names = cmp.NAMES

IDF_corpus = cmp.IDF

# PART II

# 1
def tokenization(question : str) -> list:
    tx.write_in_file('question.txt', question)
    lowercase = tx.file_in_lowercase('question.txt')
    tx.write_in_file('question.txt', lowercase)
    question_cleaned = tx.file_cleaning('question.txt')
    with open('asked_questions.txt', 'a') as f:
        f.write('QUESTION: '+ question_cleaned)
    return question_cleaned.split()

# 2
def intersection_question_corpus(question : str ) -> set:
    question_word_list = tokenization(question)
    set_question = set(question_word_list)
    set_words = set(WORDS)
    return set_question & set_words

# 3
def TF_IDF_vector_question(question : str) -> list:
    question_word_list = tokenization(question)
    set_question = set(question_word_list)
    # associting a TF to each word
    TF_question_vector = []
    for word in WORDS:
        if word in set_question:
            count = 0
            for e in question_word_list:
                if e == word:
                    count +=1
            TF_question_vector.append(count)
        else:
            TF_question_vector.append(0.0)
    # creating the T-IDF vector of the question
    TF_IDF_question = []
    for i in range(len(TF_question_vector)):
        TF_IDF_question.append(TF_question_vector[i] * IDF_corpus[WORDS[i]])

    return TF_IDF_question

# 4
def scalar_product(A:list, B:list) -> float:
    """
    Take two lists with the same size
    Return a float which is the scalar product of the two lists
    """
    product = 0
    for i in range(len(A)):
        product += A[i]*B[i]
    return product

def vector_norm(A:list) -> float:
    """
    Take a list with the same size
    Return a float which is the scalar product of the two lists
    """
    sume = 0
    for e in A:
        sume += e**2
    return math.sqrt(sume)

def similarity_calculating(A:list, B:list) -> float:
    """
    Take two lists(vectors) with the same size
    Return a float which is the similarity score between the two vector/list
    """
    product = scalar_product(A,B)
    normA = vector_norm(A)
    normB = vector_norm(B)
    return product/(normA*normB)

# 5
def most_revelant(question : str) -> str:
    """
    Take a question as parameter
    Return the name of the output file which is the most revelant
    """
    question_vector = TF_IDF_vector_question(question)
    similarity_table = []
    for j in range(len(FILES)):
        text_vector=[]
        for i in range(len(TF_IDF_MATRIX)):
            text_vector.append(TF_IDF_MATRIX[i][j])
        similarity_table.append(similarity_calculating(text_vector, question_vector))

    max_ind = 0
    for i in range(1, len(similarity_table)):
        if similarity_table[i] > similarity_table[max_ind]:
            max_ind = i

    return FILES[i]


# 6

















