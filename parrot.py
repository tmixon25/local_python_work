#Parrot
# message = input("Tell me something, and I will repeat it back to you:")
# print(message)

#Greeter
# prompt = "Tell me something, and I will repeat it back to you:"
# prompt +="\n Enter 'quit' to end the program. "
# message = ""
# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         print(message)

#Add active flag
prompt = "Tell me something, and I will repeat it back to you:"
prompt +="\n Enter 'quit' to end the program. "
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)


# name = input(prompt)
# name = input("Please enter your name: ")
# print(f"\nHello, {name}!")
