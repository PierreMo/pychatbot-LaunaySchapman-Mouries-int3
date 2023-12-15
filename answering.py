import text_treatment as tx
import computations as cmp

def tokenization(question : str) -> list:
    tx.write_in_file('question.txt', question)
    lowercase = tx.file_in_lowercase('question.txt')
    tx.write_in_file('question.txt', lowercase)
    question_cleaned = tx.file_cleaning('question.txt')
    return question_cleaned.split()

def intersection_question_corpus(question : str) -> set:
    question_word_list = tokenization(question)
    set_question = set(question_word_list)
    IDF_dict = cmp.IDF_creating('./cleaned/')
    set_words = set(IDF_dict.keys())
    print(IDF_dict)
    print(set_words)
    return set_question & set_words

def TF_IDF_vector():
    