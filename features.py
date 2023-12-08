from computations import *
from text_treatment import *

TF_IDF_matrix, words, files = TF_IDF_creating("./cleaned/")
names = finding_names(files)
def least():
    liste_somme = []
    # temporary will be replaced by a min
    for i in range(len(TF_IDF_matrix)):
        liste_somme.append(sum(TF_IDF_matrix[i]))
    least = min(liste_somme)
    unimportants_index = []
    for k in range(len(liste_somme)):
        if liste_somme[k] == least:
            unimportants_index.append(k)
    unimportants = []
    for e in unimportants_index:
        unimportants.append(words[e])
    return unimportants
