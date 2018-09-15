import pyautogui  as gui
from selenium import webdriver
from bs4 import BeautifulSoup
import time
driver = webdriver.Chrome("/media/cheatcode/0E2286E45B543E69/Projects/Python/Python/Typingbolt/chromedriver")
driver.get('https://www.typingbolt.com/')
time.sleep(1)
https=driver.page_source
soup= BeautifulSoup(https,'html.parser')
a=soup.find('ul',{'id':'characters'})
b=list(a.text)
print(b)
gui.moveTo(280,393)
gui.click()
for i in b:
	if(i=='\xa0'):
		i=' '
	gui.press(i)

