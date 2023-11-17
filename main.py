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










