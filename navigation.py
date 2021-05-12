import unittest
from selenium import webdriver
from time import sleep

class CompareProducts(unittest.TestCase):

    def setUp(self): # aqui se prepara el entorno para la prueba
        self.driver = webdriver.Chrome(executable_path= r'./chromedriver.exe')
        driver = self.driver #Reasignamos la variable para invocarla mas facil
        driver.implicitly_wait(2)
        driver.maximize_window() #esto ayuda en caso de que los elmentos cambien se posicion al maximizar la ventana
        driver.get('https://google.com/')

    def test_compare_products_removal_alert(self):
        driver = self.driver

        search_field = driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys('platzi')
        search_field.submit()

        sleep(5)
        driver.back()
        sleep(5)
        driver.forward()
        sleep(5)
        driver.refresh()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity = 2)