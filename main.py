import os
import inquirer
from stringsearch import string_search
from regsearch import reg_search
from indexsearch import index_search
from timer import timer

#Gather files to be searched

directory = 'sample_text/'

file_list = []


for file_name in os.listdir(directory):
  file_path = os.path.join(directory, file_name)
  file_list.append(file_path)


print(file_list)

search_term = ""

#Take in user data
while len(search_term) is 0:
    search_term = input("Enter the search term: ").lower()
    print("Please enter a valid search parameter")

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
    result = string_search(search_term, file_list)
    print(result)
elif answer["search_method"] == "Regular Expression":
    result = reg_search(search_term, file_list) 
    print(result)
elif answer["search_method"] == "Indexed":
    result = index_search(search_term, file_list)
    print(result)
else:
    print(answer["search_method"] + "is not a valid selection")

end = timer()

elsapsed_time = end - start

print("Elapsed Time: " + str(elsapsed_time) + " MS") 

  
