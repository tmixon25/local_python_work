prompt = "Please enter a city that you have visited:"
prompt +="\n Enter 'quit' to end the program. "

while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")