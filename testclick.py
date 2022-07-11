from selenium import webdriver
import selenium
import os

driver = webdriver.Chrome(os.getcwd() + "/chromedriver")
driver.get("https://secure.runescape.com/m=hiscore_oldschool/hiscorepersonal");
username = driver.find_element_by_name("user1")
username.send_keys("Link Caster")
driver.find_element_by_name("submit").click(); #using Selenium click button method
