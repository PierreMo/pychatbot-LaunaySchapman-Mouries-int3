from functions import *
from text_treatment import *

## PART I ##

# Menu

print("To show :" + "\n"
      "- The list of leasts important words : Least" + "\n"
      "- The list of more important words : More" + "\n"
      "- The most repeated word(s) by President Chirac : Chirac" + "\n"
      "- The name(s) of the president(s) who spoke of the 'Nation' and the one who repeated it the most times : Nation" + "\n"
      "- The first president to talk about climate (“climat”) and/or ecology (“écologie”) : Climate " + "\n"
      "- the so-called 'unimportant' words : Unimportant" + "\n"
      "- which word(s) did all the president mention : All"
)

user_input = input()

TF_IDF_matrix, words, files = TF_IDF_creating("./cleaned/")
names = text_treatment.finding_names(files)

match user_input :
      case "Least" :
            liste_somme = []
            #temporary will be replace by a min
            for i in range(len(TF_IDF_matrix)):
                  liste_somme.append(sum(TF_IDF_matrix[i]))
            print(liste_somme)
            least = min(liste_somme)
            unimportants_index = []
            for k in range(len(liste_somme)):
                  if liste_somme[k] == least:
                        unimportants_index.append(k)
            unimportants = []
            for e in unimportants_index:
                  unimportants.append(words[e])



            print(unimportants)
            print(len(unimportants))
            print(words[liste_somme.index(least)])





      case "More" :
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
            print_list(toprint)

      case "Chirac":
            # Obtaining the speeches file of chirac
            chirac_speeches_files = [i for i in range(len(files)) if 'Chirac' in files[i]]
            # Getting the TF dict of the speeches
            chirac_TFs = [TF_creating(text_treatment.read_str_in_file("./cleaned/"+files[file_ind])) for file_ind in chirac_speeches_files]
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
            print_list(maxi_words)

      case "Nation":
            # taking the TF scores of the different texts (dictionnary)
            TF_list = []
            for file in files:
                  destination = "./cleaned/" + file
                  text = text_treatment.read_str_in_file(destination)
                  TF_list.append(TF_creating(text))

            # index of presidents who spoke about nation (index coherent to names and files)
            list_index_nation = []
            for i in range(len(files)):
                  if "nation" in TF_list[i]:
                        list_index_nation.append(i)

            print(names)
            print(list_index_nation)

            # Taking the names corresponding to the index and displaying the names
            president_nation = [names[e] for e in list_index_nation]
            print('The presidents who said Nation are:')
            print_list(president_nation)

            # finding the one who said it the most
            maxi_ind = list_index_nation[0]
            maxi_val = TF_list[list_index_nation[0]]['nation']
            for index in list_index_nation[1:]:
                  if TF_list[index]['nation'] > maxi_val:
                        maxi_ind = index
                        maxi_val = TF_list[index]['nation']

            print('The president who said the word nation the most is', names[maxi_ind])




            print('The president who say the most the word Nation is','')
      case "Climate":
            print()
      case "Unimportant":
            print()
      case "All":
            print()
      case other:
            print("Enter a word of the list please")
                               

"""data, mots, noms = TF_IDF_creating("./cleaned/")
for i in range(len(data)):
      print(mots[i], data[i], end=', \n')
"""