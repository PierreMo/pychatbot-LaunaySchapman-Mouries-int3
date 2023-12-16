# In this module there are the features to develop in the part I of the project

import computations as cmp
import text_treatment as tx

# importation of IDF matrix from computations.py and associated row index, column index
TF_IDF_MATRIX, WORDS, FILES = cmp.TF_IDF_MATRIX, cmp.WORDS, cmp.FILES
# importation of the associated names (list with duplication)
names = cmp.NAMES

# taking the TF scores of the different texts (dictionnary)
TF_list = []
for file in FILES:
      destination = "./cleaned/" + file
      text = tx.read_str_in_file(destination)
      TF_list.append(cmp.TF_creating(text))

def least():
    liste_somme = []
    # temporary will be replaced by a min
    for i in range(len(TF_IDF_MATRIX)):
        liste_somme.append(sum(TF_IDF_MATRIX[i]))
    least = min(liste_somme)
    unimportants_index = []
    for k in range(len(liste_somme)):
        if liste_somme[k] == least:
            unimportants_index.append(k)
    unimportants = []
    for e in unimportants_index:
        unimportants.append(WORDS[e])
    return unimportants

def finding_highest_tfidf() -> list:
    maxi = TF_IDF_MATRIX[0][0]
    pos = {0}
    for i in range(len(TF_IDF_MATRIX)):
          for j in range(len(FILES)):
                cible = TF_IDF_MATRIX[i][j]
                if cible > maxi:
                      maxi = TF_IDF_MATRIX[i][j]
                      pos = {i}
                elif cible == maxi:
                      pos.add(i)
    toprint = [WORDS[e] for e in list(pos)]
    return toprint

def finding_highest_tf_txtname(element : str) -> list:
    # Obtaining the speeches file in which element appears in the file name
    chirac_speeches_files = [i for i in range(len(FILES)) if str(element) in FILES[i]]
    # Getting the TF dict of the speeches
    chirac_TFs = [cmp.TF_creating(tx.read_str_in_file("./cleaned/" + FILES[file_ind])) for file_ind in chirac_speeches_files]
    # summing the dictionnary
    chirac_TF_sum = {}
    for dictio in chirac_TFs:
        for word in dictio:
            if word in chirac_TF_sum:
                chirac_TF_sum[word] += dictio[word]
            else:
                chirac_TF_sum[word] = dictio[word]
    # Finding the max value in the sum
    maxi_val = 0
    maxi_words = ['']
    for key in chirac_TF_sum:
        if chirac_TF_sum[key] > maxi_val:
            maxi_val = chirac_TF_sum[key]
            maxi_words = [key]
        elif chirac_TF_sum[key] == maxi_val:
            maxi_words.append(key)
    return maxi_words



def nation() -> tuple:
    # index of presidents who spoke about nation (index coherent to names and files)
    # creating a dictionnary in which key are president who spoke about nation and value is the number of time he spoke about it
    # we need to do it because some president have many speeches
    dictio_nation = {}
    for i in range(len(FILES)):
          if "nation" in TF_list[i]:
                if names[i] in dictio_nation:
                    dictio_nation[names[i]] += TF_list[i]['nation']
                else:
                    dictio_nation[names[i]] = TF_list[i]['nation']

    president_nation = list(dictio_nation.keys())
    # finding the one who said it the most
    maxi_name = president_nation[0]
    for president in dictio_nation:
          if dictio_nation[president] > dictio_nation[maxi_name]:
                maxi_name = president

    return president_nation, maxi_name


def climat() -> list:
    print(TF_list)
    # index of presidents who spoke about nation (index coherent to names and files)
    # creating a dictionnary in which key are president who spoke about nation and value is the number of time he spoke about it
    # we need to do it because some president have many speeches
    set_climat = set()
    for i in range(len(FILES)):
          if "écologie" in TF_list[i] or "climat" in TF_list[i]:
                set_climat.add(names[i])

    president_climat = list(set_climat)

    return president_climat


def all_said() -> list:
    unimportant = least()
    all_mentioned = []
    for word in WORDS:
        print(word)
        isin = True
        i = 0
        while isin and i<len(TF_list):
            if word not in TF_list[i]:
                print(word)
                print()
                isin = False
            i+=1

        if isin and word not in unimportant:
            all_mentioned.append(word)

    return all_mentioned
