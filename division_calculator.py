# try:
#     print (5/0)
# except ZeroDivisionError:
#     print("You cannot divide by Zero dummy!")

#####
#Second part
#########
print("Give me 2 numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number:")
    if first_number == 'q':
        break
    second_number = input("Second number:")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You cannot divide by zero.")
    else:
        print(answer)