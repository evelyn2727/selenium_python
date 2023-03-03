from selenium import webdriver

# crear una instancia de WebDriver para Chrome
driver = webdriver.Chrome(executable_path="C:\chromedriver\chromedriver.exe")
driver.get("https://www.python.org/")
driver.close()