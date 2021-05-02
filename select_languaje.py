import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select # esta libreria es necesaria para manejar los select

class LanguageOptions(unittest.TestCase):

    def setUp(self): # aqui se prepara el entorno para la prueba
        self.driver = webdriver.Chrome()
        driver = self.driver #Reasignamos la variable para invocarla mas facil
        driver.implicitly_wait(2)
        driver.maximize_window() #esto ayuda en caso de que los elmentos cambien se posicion al maximizar la ventana
        driver.get('http://demo-store.seleniumacademy.com/')

    def test_select_language(self):
        exp_options = ['English', 'French', 'German']
        act_options = []

        select_language = Select(self.driver.find_element_by_id('select-language'))

        self.assertEqual(3, len(select_language.options)) # nos aseguramos que tenga la misma cantidad

        for option in select_language.options:
            act_options.append(option.text)# Los agregamos a la lista 

        self.assertListEqual(exp_options, act_options) # comparamos la lista

        self.assertEqual('English', select_language.first_selected_option.text) #aseguramos que el lenguaje selecionado sea el ingles

        select_language.select_by_visible_text('German') # Escogemos por su nombre

        self.assertTrue('store=german' in self.driver.current_url)
        # Esta seria una segunda manera de hacerlo sabiendo el indice del elemento que queremos escoger
        select_language = Select(self.driver.find_element_by_id('select-language'))
        select_language.select_by_index(0)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity = 2)