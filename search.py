import inquirer


search_term = input("Enter the search term: ") 



questions = [
  inquirer.List('size',
                message="What size do you need?",
                choices=['Jumbo', 'Large', 'Standard', 'Medium', 'Small', 'Micro'],
            ),
]
answers = inquirer.prompt(questions)



print (answer["search_method"])
print (search_term)