from bot import Bot
from selenium import webdriver

bot_username = ""
bot_password = ""
bot_driver = webdriver.Firefox()

person_to_follow = ""

bot = Bot(bot_username, bot_password, bot_driver)
bot.login()
bot.follow(person_to_follow)
