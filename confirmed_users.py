#Start with a user list and empty list
unconfirmed_users = ['alice','brian','candace']
confirmed_users = []

#Verify and move unconfirmed users
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

#Display confirmed users
print("\n The following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())