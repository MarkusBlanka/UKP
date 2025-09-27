number_of_statements = input()
list_statements = []
improved_statements = []

for i in range(int(number_of_statements)):
    user_input = input()
    list_statements.append(user_input)

for statement in list_statements:
    number_found = False
    improved_statement = statement
    for word in statement.split():
        try:
            amount = float(word)
            amount += 1
            improved_statement = improved_statement.replace(word, f"{round(amount)}")
            number_found = True
        except ValueError:
            continue
    improved_statement += "!"
    improved_statements.append(improved_statement)

for statement in improved_statements:
    print(statement)

