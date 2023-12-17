""" This module allowed to transform a text into words space separated """

# module for dealing with files:
import os

def list_of_files(directory : str, extension : str) -> list:
    '''
    Function which takes a directory and a type of file (extension) as parameters.
    It returns the name of all files which correspond to the extension in the given directory.
    '''
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names

def finding_names(files_names : list) -> list:
    '''
    Take a list of files names such as Nomination_[president's name][number].txt
    Return a list containing once the associated names
    '''
    names = set()
    for file in files_names:
        # taking the string with Nomination_ and .txt
        name= file[11:-4]
        # removing the number at end if there is one
        if 48 <= ord(name[-1]) <= 57:
            name = name[:-1]
        names.add(name)
    return list(names)
def associating_names(files_names : list) -> list:
    '''
    Take a list of files names such as Nomination_[president's name][number].txt
    Return a list containing the associated names in the same order than the entered
    '''
    names = []
    for file in files_names:
        # taking the string with Nomination_ and .txt
        name= file[11:-4]
        # removing the number at end if there is one
        if 48 <= ord(name[-1]) <= 57:
            name = name[:-1]
        names.append(name)
    return list(names)

def print_list(L : list):
    '''
    Function which display a list properly (from Lab 5)
    '''
    if L:
        for e in L[:-1]:
            print(e, end=', ')
        print(L[-1], end='.\n')
    else:
        print('Your list is empty')
def new_folder(name):
    '''
    Take a string
    Create a new folder(named by the parameter)
    do nothing if it already exists (I saw how to catch an error last year)
    '''
    try :
        os.mkdir('./'+name)
    except FileExistsError:
       pass

def file_in_lowercase(file :str) -> str:
    '''
    Function which take as input a full file name.
    Return the content of the file as a string with punctuation sign and with all letters in lowercase
    '''
    with open(file, 'r') as f:
        content = f.readlines()
    #cleaning
    content_str = ''
    for line in content:
        #removing \n
        line = line[:-1]
        #cleaning character by character for each case
        for char in line:
            # if upercase -> lowercase
            if 65 <= ord(char) <= 90:
                content_str += chr(ord(char) +32)
            # dealing with special character of French language
            elif char in 'ÈÉœÀÊÇÔÙ':
                match char:
                    case 'È':
                        content_str += "è"
                    case 'É':
                        content_str += "é"
                    case 'œ':
                        content_str += "oe"
                    case 'À':
                        content_str += "à"
                    case 'Ê':
                        content_str += "ê"
                    case 'Ç':
                        content_str += "ç"
                    case 'Ô':
                        content_str += "ô"
                    case 'Ù':
                        content_str += "ù"
            # else the character is a lowercase or a number, we add it as it is
            else:
                content_str += char
    return content_str


# Functions for text interaction
def write_in_file(file:str, content : str):
    '''
    Take a destination path of txt file and a string as parameter.
    Write the string in the file.
    '''
    with open(file, 'w') as f:
        f.write(content+'\n')
def read_str_in_file(file:str) -> str:
    '''
    Take a destination path of txt file as parameter.
    Return the content of the file as a string without the last character (\n often)
    This is made to deal with one line files
    '''
    with open(file, 'r') as f:
        #, encoding='utf-8'
        result = f.readline()[:-1]
    return result

def file_cleaning(file :str):
    '''
    Take a file name, the file has to be a one line file (only the first line is treated)
    Rewrite the file without punctuation, only words separated by spaces
    '''
    # reading the file
    line = read_str_in_file(file)
    # initializing the first word and the list of all words
    word = ''
    content = []
    # running through the text character by character and operating
    for character in line:
        if character in ["'", ' ', '-', '?', '.', ',', ';', ':', '/', '(', ')', '!', '%', '"','_', '`']:
            if word:
                content.append(word)
                word = ''
        else:
            word+=character

    # adding the word to each other separated by spaces in a string
    content_string = ''
    for word in content:
        content_string += word + ' '
    # writing the string in the appropriate file
    return content_string


def corpus_cleaning(directory):
    '''
    Take a directory (speeches for exemple), clean
    Store the content of the txt files (words separeted by spaces) present in the corpus/directory in a new folder cleaned
    '''
    # Taking the name of the files
    directory = "./speeches"
    files_names = list_of_files(directory, "txt")

    # Creating a new folder
    new_folder('cleaned')

    # Putting in lowercase and one line each file from the 'speeches' folder and storing them in the 'cleaned' repertory
    for speech_file in files_names:
        destination = "./speeches/" + speech_file
        text_lowercase = file_in_lowercase(destination)
        destination = "./cleaned/" + speech_file
        write_in_file(destination, text_lowercase)

    # Cleaning the text: removing punctuation, double spaces, rewriting the files in 'cleaned'
    for speech_file in files_names:
        destination = "./cleaned/" + speech_file
        text_cleaned = file_cleaning(destination)
        write_in_file(destination, text_cleaned)
