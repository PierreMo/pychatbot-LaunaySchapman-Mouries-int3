# In this module there are the features to develop in the part I of the project

import computations as cmp
import text_treatment as tx

TF_IDF_matrix, words, files = cmp.TF_IDF_creating("./cleaned/")
names = tx.associating_names(files)

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

def finding_highest_tfidf() -> list:
    maxi = TF_IDF_matrix[0][0]
    pos = {0}
    for i in range(len(TF_IDF_matrix)):
          for j in range(len(files)):
                cible = TF_IDF_matrix[i][j]
                if cible > maxi:
                      maxi = TF_IDF_matrix[i][j]
                      pos = {i}
                elif cible == maxi:
                      pos.add(i)
    toprint = [words[e] for e in list(pos)]
    return toprint

def finding_highest_tf_txtname(element : str) -> list:
    # Obtaining the speeches file in which element appears in the file name
    chirac_speeches_files = [i for i in range(len(files)) if str(element) in files[i]]
    # Getting the TF dict of the speeches
    chirac_TFs = [cmp.TF_creating(tx.read_str_in_file("./cleaned/" + files[file_ind])) for file_ind in chirac_speeches_files]
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
    # taking the TF scores of the different texts (dictionnary)
    TF_list = []
    for file in files:
          destination = "./cleaned/" + file
          text = tx.read_str_in_file(destination)
          TF_list.append(cmp.TF_creating(text))

    # index of presidents who spoke about nation (index coherent to names and files)
    # creating a dictionnary in which key are president who spoke about nation and value is the number of time he spoke about it
    # we need to do it because some president have many speeches
    dictio_nation = {}
    for i in range(len(files)):
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
