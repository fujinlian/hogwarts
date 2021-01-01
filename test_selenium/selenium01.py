import selenium
from selenium import webdriver


# ff

def test_selenium():
    # driver = webdriver.Chrome()
    driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
    driver.get("https://www.baidu.com/")

#test_selenium()
