# importar módulos necesarios
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# crear una instancia de WebDriver para Chrome
driver = webdriver.Chrome()

# navegar a una página web
driver.get("https://www.google.com")

# encontrar el campo de búsqueda y escribir en él
search_field = driver.find_element_by_name("q")
search_field.send_keys("ejemplo de Selenium WebDriver con Python")
search_field.send_keys(Keys.RETURN)

# esperar a que cargue la página de resultados
driver.implicitly_wait(10)

# obtener los enlaces de los resultados de búsqueda
links = driver.find_elements_by_css_selector("div.r a")

# imprimir los enlaces
for link in links:
    print(link.get_attribute("href"))

# cerrar el navegador
driver.quit()