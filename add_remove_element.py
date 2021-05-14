import unittest
from selenium import webdriver
from time import sleep
import sys

class Add_Remove(unittest.TestCase):

    def setUp(self): # aqui se prepara el entorno para la prueba
        self.driver = webdriver.Chrome(executable_path= r'./chromedriver.exe')
        driver = self.driver #Reasignamos la variable para invocarla mas facil
        driver.maximize_window() #esto ayuda en caso de que los elmentos cambien se posicion al maximizar la ventana
        driver.get('http://the-internet.herokuapp.com/')
        driver.find_element_by_link_text('Add/Remove Elements').click()

    def test_account_link(self):
        driver = self.driver

        elements_added = int(input('How many elements will you add?'))
        elements_removed = int(input('How many elements will you removed?'))
        total_elements = elements_added - elements_removed

        add_button = driver.find_element_by_xpath('//*[@id="content"]/div/button')

        sleep(3)

        for i in range(elements_added):
            add_button.click()

        for i in range(elements_removed):
            try:
                delete_button = driver.find_element_by_xpath('//*[@id="elements"]/button[1]')
                delete_button.click()
            except:
                print("You are trying to delete more elements than existent", sys.exc_info()[0])
                break
        if total_elements > 0:
            print(f'there are {total_elements} elements on screen')

        sleep(3)    

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity = 2)