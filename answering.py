import text_treatment as tx
import computations as cmp

# importation of IDF matrix from computations.py and associated row index, column index
TF_IDF_matrix, words, files = cmp.TF_IDF_matrix, cmp.words, cmp.files
# importation of the associated names (list with duplication)
names = cmp.names

IDF_corpus = cmp.IDF

# PART II

# 1
def tokenization(question : str) -> list:
    tx.write_in_file('question.txt', question)
    lowercase = tx.file_in_lowercase('question.txt')
    tx.write_in_file('question.txt', lowercase)
    question_cleaned = tx.file_cleaning('question.txt')
    return question_cleaned.split()

# 2
def intersection_question_corpus(question : str ) -> set:
    question_word_list = tokenization(question)
    set_question = set(question_word_list)
    set_words = set(words)
    return set_question & set_words

# 3
def TF_IDF_vector_question(question : str) -> list:
    question_word_list = tokenization(question)
    set_question = set(question_word_list)
    # associting a TF to each word
    TF_question_vector = []
    for word in words:
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
        TF_IDF_question.append(TF_question_vector[i]*IDF_corpus[words[i]])

    return TF_IDF_question

