from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chromedriver = 'C:\Program Files (x86)\chromedriver.exe'

driver = webdriver.Chrome(chromedriver, chrome_options=chrome_options)
#driver.implicitly_wait(1)
driver.maximize_window()
    



driver.get("http://www.google.com/search?q=" + 'oxygen benefits')
res = driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div[1]/div/div[1]/div/div[2]/div')
# print(driver.find_element_by_class_name('hgKE1c'))
ans = res.text.split('.')
#print(ans)
for i in range(2):
    print(ans[i],end='.')
