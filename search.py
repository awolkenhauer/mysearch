import os
import inquirer

file_list = []

for files in os.listdir("sample_text/"):
  file_list.append(files)

search_term = input("Enter the search term: ")

question = [
  inquirer.List('search_method',
                message="Select a search method:",
                choices=['String Match', 'Regular Expression', 'Indexed'],
            ),
]
answer = inquirer.prompt(question)

print (answer["search_method"])
print (search_term)