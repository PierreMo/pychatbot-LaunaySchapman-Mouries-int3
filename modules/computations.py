# pychatbot-LaunaySchapman-Mouries-int3
# Launay-Schapman Alexis and Pierre Mouriès

# role of the file: This module is used to compute the TF-IDF of words in a text corpus
# at the end of this file globals variables of the project are created using its functions


#### IMPORTATIONS ####
from modules import text_treatment as tx
import math

#### FUNCTIONS ####
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
    # initializing the dictionary
    IDF_dict = {}
    # running through the texts
    for file_name in files:
        # putting all the words of the text in a set
        words_in_file = set()
        for word in tx.read_str_in_file(directory+file_name).split(' '):
            words_in_file.add(word)
        # incrementing or initializing the count of words in the dictionary
        for word in words_in_file:
            if word:
                if word in IDF_dict:
                    IDF_dict[word] += 1
                else:
                    IDF_dict[word] = 1

    # computing the IDF: number of document/ number of documents in which the word appear
    nbr_doc = len(files)
    for word in IDF_dict:
        IDF_dict[word] = math.log10(nbr_doc/IDF_dict[word])
    # result in a dictionary such as word:IDF
    return IDF_dict


def TF_IDF_creating(directory : str) -> tuple:
    """
    :param directory: directory name with txt files inside
    :return: tuple, TF-IDF matrix and list of words correspoding to the lines and list of text files corresponding the columns of the matrix
    """
    # taking IDF from the IDF function
    IDF = IDF_creating(directory)
    # extracting the keys from IDF dict -> the words of the corpus
    # this list will be very useful to relate the TF-IDF present in the matrix to the associated word
    word_list = list(IDF.keys())
    # extracting the files names using text_treatment.py
    # this list will be very useful to relate the TF-IDF present in the matrix to the associated file/text
    files_names = tx.list_of_files(directory, ".txt")
    # extracting the TF of all files using the TF_creating function in a list so nice ordered
    TF_list = []
    for file in files_names:
        destination = "./cleaned/" + file
        text = tx.read_str_in_file(destination)
        TF_list.append(TF_creating(text))
    #initializing the matrix
    TF_IDF = []
    # building the matrix, a row per word and a column per file
    for word in word_list:
        TF_IDF.append([])
        for i in range(len(files_names)):
            # multiplying the TF of the word in the file by the IDF of the word in the corpus
            # 0.0 if word is not in the text
            if word in TF_list[i]:
                TF_IDF[-1].append(TF_list[i][word] * IDF[word])
            else:
                TF_IDF[-1].append(0.0)
    return TF_IDF, word_list, files_names


#### CREATING GLOBALS VARIABLES ####
# cleaning the files thanks to our text_treatment module (file cleaned are in the cleaned directory)
tx.corpus_cleaning('speeches')

# computing useful globals variables
IDF = IDF_creating('./cleaned/')
TF_IDF_MATRIX, WORDS, FILES = TF_IDF_creating("./cleaned/")
NAMES = tx.associating_names(FILES)
