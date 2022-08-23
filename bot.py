from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class Bot:
    def __init__(self, username: str, password: str, driver) -> None:
        self.username = username
        self.password = password
        self.bot = driver

    def login(self):
        bot = self.bot
        bot.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)
        bot.find_element(By.CLASS_NAME, "aOOlW.bIiDR").click()
        time.sleep(5)
        username_box = bot.find_element(By.NAME, "username")
        password_box = bot.find_element(By.NAME, "password")
        username_box.clear()
        password_box.clear()
        username_box.send_keys(self.username)
        password_box.send_keys(self.password)
        time.sleep(5)
        bot.find_element(By.CLASS_NAME, "sqdOP.L3NKy.y3zKF").click()
        time.sleep(10)
        bot.find_element(By.CLASS_NAME, "sqdOP.L3NKy.y3zKF").click()
        time.sleep(10)
        bot.find_element(By.CLASS_NAME, "_a9--._a9_1").click()
        time.sleep(10)

    def follow(self, to_follow: str) -> None:
        search_box = self.bot.find_element(By.CLASS_NAME, "_aawc._aawd").click()
        search_box = self.bot.find_element(By.CLASS_NAME, "_aauy")
        search_box.clear()
        search_box.send_keys(to_follow)
        time.sleep(2)
        search_box.send_keys(Keys.ENTER)
        time.sleep(2)
        search_box.send_keys(Keys.ENTER)
        time.sleep(2)
        search_box = self.bot.find_element(By.CLASS_NAME, "_aacl._aaco._aacw._adda._aad6._aade").click()

