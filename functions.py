import os

def list_of_files(directory : str, extension : str) -> list:
    '''Function which takes a directory and a type of file (extension) as parameters.
        It returns the name of all files which correspond to the extension in the given directory. '''
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names

def finding_names(files_names : list) -> list:
    ''' Take a list of files names such as Nomination_[president's name][number].txt
    '''
    names = set()
    for file in files_names:
        # taking the string with Nomination_ and .txt
        name = file[11:-4]
        # removing the number at end if there is one
        if 48 <= ord(name[-1]) <= 57:
            name = name[:-1]
        names.add(name)
    return list(names)

def print_list(L : list):
    '''
    Function which display a list properly (from Lab 5)
    '''
    for e in L[:-1]:
        print(e, end=', ')
    print(L[-1])

def new_folder(name):
    '''
    Creating a new folder, do nothing if it already exists (I saw how to catch an error last year)
    '''
    try :
        os.mkdir(name)
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
            else:
                content_str += char
    return content_str


# Functions for text interaction
def write_in_file(file:str, content : str):
    with open(file, 'w') as f:
        f.write(content)
def read_str_in_file(file:str) -> str:
    with open(file, 'r') as f:
        return f.readline()[:-1]

def file_cleaning(file :str) -> str:
    '''
    Take a file name, the file has to be a one line file (only the first line in treated)
    Return the content of the file without punctuation, only words separated by spaces, be careful there is a space at the end of the string
    '''
    with open(file, 'r') as f:
        line = f.readline()

    word = ''
    content = []
    for character in line:
        if character in ["'", ' ', '-', '?', '.', ',', ';', ':', '/', '(', ')', '!', '%', '"']:
            content.append(word)
            word = ''
        else:
            word+=character

    content_string = ''
    for word in content:
        if word != '':
            content_string += word + ' '

    return content_string

def TF_creating(text : str) -> dict:
    '''
    function that takes a string as a parameter
    returns a dictionary associating with each word the number of times it appears in the string
    '''
    TFdictionnary = {}
    for word in text.split(' '):
        if word in TFdictionnary:
            TFdictionnary[word] = TFdictionnary[word] + 1
        else:
            TFdictionnary[word] = 1
    return TFdictionnary

def IDF_creating(TFs : list) -> dict:
    '''
    Take a list of dictionnary: for each file the list contain the TF dictionnary of the file
    returns a dictionary associating the IDF score with each word
    '''





















