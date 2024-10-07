import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

profile_path = ""  # Replace this with your actual profile path
options = Options()
options.profile = profile_path

browser = webdriver.Chrome(options=options)
browser.get("https://www.bing.com/")

search_box = browser.find_element(By.NAME, "q") 
for i in range(0,30):
    search_box.clear() 
    search_box.send_keys("Fortnite Season" + str(i))
    search_box.send_keys(Keys.RETURN)
    time.sleep(7)
    search_box = browser.find_element(By.NAME, "q")

browser.close()