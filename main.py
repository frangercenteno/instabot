import getpass
from instabot import InstaBot  

accounts = []

def getAccounts(num):   
    for i in range(num):
        user = input(f"User {i}: ")
        accounts.append(user)
        print(accounts)


if __name__ == "__main__":
    username = input("Enter Username: ")
    password = getpass.getpass("Enter Password: ")
    Bot = InstaBot(username,password)
    Bot.login()
    opc = input("""     Choice 1 option\n1=Win Followers\n2=Unfollowers accounts\n===> """)
    if opc == "1":
        num = int(input("Number of accounts: ")) 
        getAccounts(num)
        allAccounts = int(input("Number of accounts to follow: "))
        if num == accounts.__len__():
            Bot.winFollowers(accounts,allAccounts)
            exit()
    elif opc == "2":
        num = int(input("Number of accounts to unfollow"))
        Bot.unfollow(num)
        exit()
    else:
        print("Invalid value")
        exit()
