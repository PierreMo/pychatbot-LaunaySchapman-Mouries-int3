""" This module is used to compute the TF-IDF of words in a text corpus"""

import text_treatment as tx
import math

tx.corpus_cleaning('speeches')

def TF_creating(text : str) -> dict:
    '''
    function that takes a string as a parameter
    returns a dictionary associating with each word the number of times it appears in the string
    '''
    # initialisation of the dictionnary
    TFdictionnary = {}
    # running through the words of the text
    for word in text.split(' '):
        # counting the occurences of the differents words in the dictionnary
        if word in TFdictionnary:
            TFdictionnary[word] += 1
        else:
            TFdictionnary[word] = 1
    return TFdictionnary

def IDF_creating(directory : str) -> dict:
    '''
    Take a name of directory
    returns a dictionary associating the IDF score with each word present in the txt files of the directory
    '''
    # find every txt file and store their names in a list
    files = tx.list_of_files(directory, ".txt")
    IDF_dict = {}
    for file_name in files:
        words_in_file = set()
        for word in tx.read_str_in_file(directory+file_name).split(' '):
            words_in_file.add(word)
        for word in words_in_file:
            if word in IDF_dict:
                IDF_dict[word] += 1
            else:
                IDF_dict[word] = 1
    nbr_doc = len(files)
    for word in IDF_dict:
        IDF_dict[word] = math.log10(nbr_doc/IDF_dict[word])
    return IDF_dict


def TF_IDF_creating(directory : str) -> tuple:
    IDF = IDF_creating(directory)
    word_list = list(IDF.keys())
    files_names = tx.list_of_files(directory, ".txt")
    TF_list = []
    for file in files_names:
        destination = "./cleaned/" + file
        text = tx.read_str_in_file(destination)
        TF_list.append(TF_creating(text))
    TF_IDF = []
    for word in word_list:
        TF_IDF.append([])
        for i in range(len(files_names)):
            if word in TF_list[i]:
                TF_IDF[-1].append(TF_list[i][word] * IDF[word])
            else:
                TF_IDF[-1].append(0.0)

    return TF_IDF, word_list, files_names
