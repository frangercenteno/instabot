from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import getpass

class InstaBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome(ChromeDriverManager().install())

    def login(self):
        bot = self.bot
        bot.get('https://www.instagram.com/accounts/login/')
        time.sleep(3)
        # set user and password to Instagram form
        username = bot.find_element_by_name('username').send_keys(self.username)
        password = bot.find_element_by_name('password').send_keys(self.password)
        time.sleep(3)
        bot.find_element_by_name('password').send_keys(Keys.RETURN)
        time.sleep(3)

    def winFollowers(self, accounts, countFollowers):
        self.accounts = accounts
        bot = self.bot
        for account in accounts:
            bot.get('https://www.instagram.com/' + account)
            time.sleep(3)
            bot.find_elements_by_xpath('//a[@href="/' + account + '/followers/"]')[0].click()
            time.sleep(3)
            for i in range(countFollowers):
                bot.find_elements_by_xpath('//button[@class="sqdOP  L3NKy   y3zKF     "]')[i].click()
                

accounts = []

def getAcounts(num):   
    for i in range(num):
        user = input(f"User {i}: ")
        accounts.append(user)
        print(accounts)


if __name__ == "__main__":
    username = input("Enter Username: ")
    password = getpass.getpass("Enter Password: ")
    Bot = InstaBot(username,password)
    Bot.login()
    opc = input("""     Choise 1 option\n1=Win Followers\n2=Unfollowers accounts\n===> """)
    if opc == "1":
        num = int(input("Number of acounts: ")) 
        getAcounts(num)
        allAcounts = int(input("Number of acounts to follow: "))
        if num == accounts.__len__():
            Bot.winFollowers(accounts,allAcounts)
            exit()
    elif opc == "2":
        numm = int(input("Number of accounts to unfollow"))
        Bot.unfollow(numm)
        exit()
    else:
        print("Invalid value")
        exit()
