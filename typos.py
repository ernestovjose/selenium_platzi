import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from time import sleep
import sys

class CompareProducts(unittest.TestCase):

    def setUp(self): # aqui se prepara el entorno para la prueba
        self.driver = webdriver.Chrome(executable_path= r'./chromedriver.exe')
        driver = self.driver #Reasignamos la variable para invocarla mas facil
        driver.maximize_window() #esto ayuda en caso de que los elmentos cambien se posicion al maximizar la ventana
        driver.get('http://the-internet.herokuapp.com/')
        driver.find_element_by_link_text('Typos').click()

    def test_dynamic_controls(self):
        driver = self.driver

        paragraph_to_check = driver.find_element_by_css_selector('#content > div > p:nth-child(3)')
        text_to_check = paragraph_to_check.text
        print(text_to_check)

        tries = 1
        found = False
        correct_text = "Sometimes you'll see a typo, other times you won't."

        while text_to_check != correct_text:
            paragraph_to_check = driver.find_element_by_css_selector('#content > div > p:nth-child(3)')
            text_to_check = paragraph_to_check.text
            driver.refresh()

        while not found:
            if text_to_check == correct_text:
                tries += 1
                driver.refresh()
                found = True

        self.assertEqual(found, True)

        print(f'it took {tries} tries to find the typo')            

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity = 2)