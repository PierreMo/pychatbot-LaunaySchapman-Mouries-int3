import text_treatment as tx
import features
import answering

## PART I ##

# Menu
question = "Comment est-ce que l'on peut écrire ça?"
print(answering.tokenization(question))
print(answering.intersection_question_corpus(question))
print(answering.TF_IDF_vector_question(question))
print(answering.similarity_calculating(answering.TF_IDF_vector_question(question),answering.TF_IDF_vector_question("Pourquoi est-ce que tu peut écrire ça?")))
print(answering.most_revelant(" Peux-tu me dire comment une nation peut-elle prendre soin du climat?"))
while True:
      print("To show :" + "\n"
            "- The list of leasts important words: Least" + "\n"
            "- The list of more important words (highest TD-IDF): More" + "\n"
            "- The most repeated word(s) by President Chirac : Chirac" + "\n"
            "- The name(s) of the president(s) who spoke of the 'Nation' and the one who repeated it the most times: Nation" + "\n"
            "- The first president to talk about climate (“climat”) and/or ecology (“écologie”): Climate " + "\n"
            "- Word(s) which all the president mention (excepti the so-called 'unimportant' words): All"
      )

      user_input = input()
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
                  names_nation, name = features.nation()
                  print('The presidents who said the word Nation are', end=' ')
                  tx.print_list(names_nation)
                  print('The president who said the most the word Nation is', name)
            case "Climate":
                  names_climat = features.climat()
                  print('The presidents who spoke about ecology or climate are', end=' ')
                  tx.print_list(names_climat)
            case "All":
                  words_mention = features.all_said()
                  print('The presidents all say: ', end=' ')
                  tx.print_list(words_mention)
            case other:
                  print("Enter a word of the list please")
