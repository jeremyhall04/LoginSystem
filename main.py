from getpass import getpass
from get_users import create_user, check_user


print("\nPlease Log-in. To create an account, please insert Username '/'")
complete = False
pass_complete = False
password = None
valid_user = False
user_attempt = 0
skip = False

while complete != True:
    username = input("Username: ")
    if username == "/":
        print("     Creating new account!")
        username = create_user()

    (valid_user, password) = check_user(username, valid_user)
    if valid_user == True:
        complete = True

while pass_complete != True:
    pass_attempts = 0
    pw_in = getpass()
    if password != pw_in:
        print("Incorrect Password")
    else:
        break

print("\nYou have successfully logged in!")
