import names
import colorama
import time as t
import random
import requests
import pyautogui
from colorama import Fore, Back, Style
from colorama import init
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.options import Options
init()
print(Fore.GREEN + 'Instagram Autoliker script\n**************************************\n**************************************')
print(Fore.RED + 'Enter only correct login and password, else script will not work')
print(Fore.GREEN)
logincha = input("Enter your login: ")
password1 = input("Enter your password: ")
path = input("Full link to the whereabouts of chromedriver: \n Change \\ to / on your link ")
hashtag = input("Enter hashtag without #: ")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(executable_path=path, options=options)




driver.get('https://www.instagram.com/')

t.sleep(3)
login = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
login.send_keys(logincha)

password = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
password.send_keys(password1)

continuebtn = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
continuebtn.click()

t.sleep(2)
pyautogui.sleep(2)
pushinput = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/nav/div[2]/div/div/div[2]/input')
pushinput.send_keys("#"+hashtag)


t.sleep(2)
pyautogui.sleep(2)
clickHASHTAG = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a')
clickHASHTAG.click()
t.sleep(2)
pyautogui.sleep(2)
clickbtn = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/main/article/div[1]/div/div/div[1]/div[2]')
clickbtn.click()
while 1==1:
	t.sleep(0.5)
	pyautogui.sleep(0.5)
	actionlike = driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button')
	actionlike.click()
	actionmove = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div/div/div[2]/button')
	actionmove.click()
