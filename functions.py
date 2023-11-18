import math
import text_treatment
def TF_creating(text : str) -> dict:
    '''
    function that takes a string as a parameter
    returns a dictionary associating with each word the number of times it appears in the string
    '''
    TFdictionnary = {}
    for word in text.split(' '):
        if word in TFdictionnary:
            TFdictionnary[word] += 1
        else:
            TFdictionnary[word] = 1
    return TFdictionnary

def IDF_creating(directory : str) -> dict:
    '''
    Take a name of directory
    returns a dictionary associating the IDF score with each word
    '''
    # find every txt file and store their neames in a list
    files = text_treatment.list_of_files(directory, ".txt")
    IDF_dict = {}
    for file_name in files:
        words_in_file = set()
        for word in text_treatment.read_str_in_file(directory+file_name).split(' '):
            words_in_file.add(word)
        for word in words_in_file:
            if word in IDF_dict:
                IDF_dict[word] += 1
            else:
                IDF_dict[word] = 1
    nbr_doc = len(files)
    for word in IDF_dict:
        IDF_dict[word] = math.log(nbr_doc/IDF_dict[word])
    return IDF_dict























