https://github.com/PierreMo/pychatbot-LaunaySchapman-Mouries-int3

The purpose of this project is to analyse a corpus of text and to be able to find a sentence corresponding to a question in the corpus.

The texts are some speeches made by french presidents they are in the speeches directory.

main.py is a meny using 4 other python file to make you able to use the functionalities.

in the modules directory:
text_treatment.py is used to deal with files and string it can read, write, display and especially clean a text (remove ponctuations and upercase)
computations.py computes a TF-IDF matrix, a IDF dictionarry and a TF list. It creates also global variables which are used by all others modules. it first use text_treatment.py to clean the texts in a cleaned directory
features.py is composed of functions of text analysis using the global variables
answering.py is able to compute the TF-IDF of a question and to find the appropriate sentence in the appropriate text. there also an historic of questions functionality

The major part of these functions is reusable, the code is commented so feel free to do what you want

made by Pierre