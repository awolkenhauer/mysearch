import os
import inquirer
from stringsearch import string_search
from regsearch import reg_search
from indexsearch import index_search
from timer import timer

#Gather files to be searched
file_list = []

for files in os.listdir("sample_text/"):
  file_list.append(files)


#Take in user data
search_term = input("Enter the search term: ") 

question = [
  inquirer.List('search_method',
                message="Select a search method:",
                choices=['String Match', 'Regular Expression', 'Indexed'],
                carousel = True,
            ),
]
answer = inquirer.prompt(question)

start = timer()

if answer["search_method"] == "String Match":
    result = string_search()
    print(result)
elif answer["search_method"] == "Regular Expression":
    result = reg_search()
    print(result)
    print(answer["search_method"])
elif answer["search_method"] == "Indexed":
    result = index_search()
    print(result)
    print(answer["search_method"])
else:
    print(answer["search_method"] + "is not a valid selection")

end = timer()

elsapsed_time = end - start

print("Elapsed Time: " + str(elsapsed_time) + " MS") 

  
