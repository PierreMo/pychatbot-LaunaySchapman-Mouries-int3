# pychatbot-LaunaySchapman-Mouries-int3
# Launay-Schapman Alexis and Pierre Mouriès

# role of the file: This is the main file its purpose is to combine all the functionalities in a console menu

from modules import text_treatment as tx
from modules import features
from modules import answering

## PART I ##

# Menu

print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n"
      "░░░░░░░░░░░▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n"
      "░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n"
      "░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒░\n"
      "░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒░░░\n"
      "▒░░░░░░░░░░░▒▒▒▒▒▒░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒▒▒▒▒░░░░▒▒▒▒▒▒▒▒▒▒░░░░░▒▒\n"
      "▓▓▓▒▒░░░░░░░░░░░░░░░░░░░░░▒▒░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒░░░▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒\n"
      "▓▓▓▓▓▓▓▒░░░░░░░░░░░░░▒▒▒▒▒▒▒░░░░▒▒▒░░░░░░░░▒▒▒░░▒▒▒░░░░░░░░▒▒▒░░░░░░░░░▒▒▒░░░░░░░░▒▒▒░░▒▒▒\n"
      "▓▓▓▓▓▓▓▓▓▓░░░░░░░░▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒░░░▒▒▒░░░░░░░░▒▒▒░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒░░░▒▒▒\n"
      "▓▓▓▓▓▓▓▓▓▓░░░░░░░░▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒░░░░░░░░░░░░░▒▒▒░░░░░░░░▒▒▒░░░░░░░░░▒▒▒░░░░░░░░░░░░░▒▒▒\n"
      "▓▓▓▓▓▓▓▓▓▓░░░░░░░░▒▒▒▒▒▒▒▒▒▒░░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░░▒▒▒░░░░░░░░▒▒▒░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░░▒▒▒\n"
      "▓▓▓▓▓▓▓▓▓▓░░░░░░░░▒▒▒▒▒▒▒▒▒░░░░░░░░▒▒▒▒▒▒▒▒▒░░░░░▒▒░░░░░░░░░▒▒░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒░░░░░▒░\n"
      "░░░▒▓▓▓▓▓▓░░░░░░░░▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n"
      "░░░░░░▒▓▓▓░░░░░░░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n"
      "░░░░░░░░░▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n"
      "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░"
)

running = True
while running:
      print('------------------------------------------------------------------------')
      print("Hi ! You can enter f to use the features of text analysis or c to use the chatBot functionalities. (s for stop)")
      user_choice = input()
      match user_choice:
            case "f":
                  print('------------------------------------------------------------------------')
                  print("Features:")
                  print("Enter a number of the list:")
                  featuring = True
                  while featuring:
                        print("Option :" + "\n"
                              "     1) The list of leasts important words." + "\n"
                              "     2) The list of more important words (highest TD-IDF)" + "\n"
                              "     3) The most repeated word(s) by President Chirac" + "\n"
                              "     4) The name(s) of the president(s) who spoke of the 'Nation' and the one who repeated it the most times" + "\n"
                              "     5) The first president to talk about climate (“climat”) and/or ecology (“écologie”)" + "\n"
                              "     6) Word(s) which all the president mention (excepti the so-called 'unimportant' words)" + "\n"
                              "     7) Main menu"
                        )

                        user_input = input()
                        match user_input :
                              case "1" :
                                    least_importants = features.least()
                                    tx.print_list(least_importants)
                              case "2" :
                                    highest_tf_idf = features.finding_highest_tfidf()
                                    tx.print_list(highest_tf_idf)

                              case "3":
                                    highest_tf_chirac = features.finding_highest_tf_txtname('Chirac')
                                    tx.print_list(highest_tf_chirac)

                              case "4":
                                    names_nation, name = features.nation()
                                    print('The presidents who said the word Nation are', end=' ')
                                    tx.print_list(names_nation)
                                    print('The president who said the most the word Nation is', name)
                              case "5":
                                    names_climat = features.climat()
                                    print('The presidents who spoke about ecology or climate are', end=' ')
                                    tx.print_list(names_climat)
                              case "6":
                                    words_mention = features.all_said()
                                    print('The presidents all say: ', end=' ')
                                    tx.print_list(words_mention)
                              case "6":
                                    featuring = False
                              case other:
                                    print("Enter a word of the list please")
            case 'c':
                  print('------------------------------------------------------------------------')
                  print("Features:")
                  chatboting = True
                  while chatboting:
                        print("You can ask a question or:"+ "\n"
                              "     - h for your historic," + "\n"
                              "     - m for the main menu" + "\n"
                              "     - c for clean your historic")
                        question = input()
                        print()
                        match question:
                              case "h":
                                    historic = answering.print_historic()
                              case 'm':
                                    chatboting = False
                              case 'c':
                                    print(answering.clean_historic())
                              case other:
                                    try:
                                          print(answering.refine_answer(question))
                                    except ZeroDivisionError:
                                          print("Sorry, I didn't understand")
            case 's':
                  running= False
            case other:
                  print("Sorry, I didn't understand")