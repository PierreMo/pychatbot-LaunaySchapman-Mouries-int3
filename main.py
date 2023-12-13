from computations import *
import text_treatment as tx
import features

## PART I ##

# Menu

print("To show :" + "\n"
      "- The list of leasts important words: Least" + "\n"
      "- The list of more important words (highest TD-IDF): More" + "\n"
      "- The most repeated word(s) by President Chirac : Chirac" + "\n"
      "- The name(s) of the president(s) who spoke of the 'Nation' and the one who repeated it the most times: Nation" + "\n"
      "- The first president to talk about climate (“climat”) and/or ecology (“écologie”): Climate " + "\n"
      "- the so-called 'unimportant' words: Unimportant" + "\n"
      "- which word(s) did all the president mention: All"
)

user_input = input()

TF_IDF_matrix, words, files = TF_IDF_creating("./cleaned/")
names = tx.finding_names(files)

match user_input :
      case "Least" :
            least_importants = features.least()
            tx.print_list(least_importants)
      case "More" :
            highest_tf_idf = features.finding_highest_tfidf()
            tx.print_list(highest_tf_idf)

      case "Chirac":
            highest_tf_chirac = features.finding_highest_tf_txtname('Chirac')
            tx.print_list(highest_tf_chirac)

      case "Nation":
            names, name = features.nation()
            print('The presidents who said the word Nation are', end=' ')
            tx.print_list(names)
            print('The president who said the most the word Nation is', name)
      case "Climate":
            print('climat', 'écologie')
            
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