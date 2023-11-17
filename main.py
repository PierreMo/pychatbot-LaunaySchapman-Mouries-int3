from functions import *

## PART I ##

# Taking the name of the files
directory = "./speeches"
files_names = list_of_files(directory, "txt")

# Finding the name of the different presidents from the names of the files and display them
presidents_names = finding_names(files_names)
#print_list(presidents_names)

# Creating a new folder
new_folder('cleaned')

# Putting in lowercase and one line each file from the 'speeches' folder and storing them in the 'cleaned' repertory
for speech_file in files_names:
    destination = "./speeches/" + speech_file
    text_lowercase = file_in_lowercase(destination)
    destination = "./cleaned/" + speech_file
    write_in_file(destination, text_lowercase)

# Cleaning the text: removing punctuation, double spaces, rewriting the files in 'cleaned'
for speech_file in files_names:
    destination = "./cleaned/" + speech_file
    text_cleaned = file_cleaning(destination)
    write_in_file(destination, text_cleaned)

# Creating a list with the TF (dictionnary of term frequency) of each file
TF_list = []
for speech_file in files_names:
    destination = "./cleaned/" + speech_file
    text = read_str_in_file(destination)
    TF_list.append(TF_creating(text))

for e in TF_list:
    print(e)


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






