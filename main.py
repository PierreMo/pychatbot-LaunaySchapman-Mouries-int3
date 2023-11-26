from functions import *
from text_treatment import *

## PART I ##

# Menu

print("To show :" + "\n"
      "- The list of least important words : Least" + "\n"
      "- The list of more important words : More" + "\n"
      "- The most repeated word(s) by President Chirac : Chirac" + "\n"
      "- The name(s) of the president(s) who spoke of the 'Nation' and the one who repeated it the most times : Nation" + "\n"
      "- The first president to talk about climate (“climat”) and/or ecology (“écologie”) : Climate " + "\n"
      "- the so-called 'unimportant' words : Unimportant" + "\n"
      "- which word(s) did all the president mention : All" + "\n"
)

user_input = input()

TF_IDF_matrix, words, files = TF_IDF_creating("./cleaned/")

match user_input :
      case "Least" :
            unimportant = []
            for i in range(len(TF_IDF_matrix)):
                  if TF_IDF_matrix[i] == [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]:
                        unimportant.append(words[i])
            print_list(unimportant)

      case "More" :
            maxi = TF_IDF_matrix[0][0]
            pos = set([0])
            for i in range(len(TF_IDF_matrix)):
                  for j in range(len(files)):
                        cible = TF_IDF_matrix[i][j]
                        if cible != None and cible > maxi:
                              maxi = TF_IDF_matrix[i][j]
                              pos = set([i])
                        elif cible == maxi:
                              pos.add(i)
            toprint = [words[e] for e in list(pos)]
            print_list(toprint)
      case "Chirac":
            # a refaire
            unimportant = []
            chirac = [i for i in range(len(files)) if 'Chirac' in files[i]]
            for j in chirac:
                  for i in range(len(TF_IDF_matrix)):
                        if TF_IDF_matrix[i][j] == 0.0:
                              unimportant.append(words[i])
            print_list(unimportant)
      case "Nation":

            files_names = text_treatment.list_of_files("./cleaned/", ".txt")
            TF_list = []
            for file in files_names:
                  destination = "./cleaned/" + file
                  text = text_treatment.read_str_in_file(destination)
                  TF_list.append(TF_creating(text))
            print()
      case "Climate":
            print()
      case "Unimportant":
            print()
      case "All":
            print()
      case other:
            print("Enter a word of the list please")
                               
"""
data, mots, noms = TF_IDF_creating("./cleaned/")
for i in range(len(data)):
      print(mots[i], data[i], end=', \n')
"""