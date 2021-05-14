import unittest
from selenium import webdriver
from time import sleep
import sys

class Dinamic_elements(unittest.TestCase):

    def setUp(self): # aqui se prepara el entorno para la prueba
        self.driver = webdriver.Chrome(executable_path= r'./chromedriver.exe')
        driver = self.driver #Reasignamos la variable para invocarla mas facil
        driver.maximize_window() #esto ayuda en caso de que los elmentos cambien se posicion al maximizar la ventana
        driver.get('http://the-internet.herokuapp.com/')
        driver.find_element_by_link_text('Disappearing Elements').click()

    def test_account_link(self):
        driver = self.driver

        option = []
        menu = 5
        tries = 1

        while len(option) < 5:
            option.clear()

            for i in range(menu):
                try:
                    option_name = driver.find_element_by_xpath(f'/html/body/div[2]/div/div/ul/li[{i + 1}]/a')
                    option.append(option_name.text)
                    print(option)
                except:
                    print(f"Option number {i + 1} is NOT FOUND")
                    tries+=1
                    driver.refresh()
        print(f"finished in {tries} tries")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity = 2)