age=72
if age<4:
    price=0
    # print("Your admission is $0.")
elif age <18:
    # print("Your admission cost is $25")
    price=25
elif age < 65:
    price=40
else:
    # print("Your admission cost is $40.")
    price=20
print(f"Your admission cost is ${price}.")