import os
import inquirer
from operator import itemgetter
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
elif answer["search_method"] == "Regular Expression":
    result = reg_search(search_term, file_list) 
elif answer["search_method"] == "Indexed":
    result = index_search(search_term, file_list)
else:
    print(answer["search_method"] + "is not a valid selection")

end = timer()

elsapsed_time = end - start

#os.system('clear')

#print("The results of the", answer["search_method"].lower(), "search are:")

print()

#for key, value in sorted(result.items(), key = itemgetter(1), reverse = True):
#    file_name = key.split('/')
#    print(file_name[1], "-", value)
#    print()

#print("Elapsed Time: " + str(elsapsed_time) + " MS") 

print()
  
