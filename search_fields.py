import unittest #esta libreria para hacer pruebas unitarias en python
from pyunitreport import HTMLTestRunner #Permite hacer reportes que seran escritos en un html
from selenium import webdriver #Y este permite llamar al driver del exporador que vamos a utilizar

class HelloWorld(unittest.TestCase):

    @classmethod # Al declarar un class method todas las pruebas se realizan en el navegador
    def setUpClass(cls): # aqui se prepara el entorno para la prueba
        cls.driver = webdriver.Chrome()
        driver = cls.driver #Reasignamos la variable para invocarla mas facil
        # driver.get('http://10.36.237.137/')
        # driver.get('https://ed.team/')
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window() #esto ayuda en caso de que los elmentos cambien se posicion al maximizar la ventana
        driver.implicitly_wait(10) #Aqui indicamos que espere 10 seg antes de tomar alguna accion


    def test_search_text_field(cls): # aqui se encuentran las acciones o serie de acciones
        search_field = cls.driver.find_element_by_id("search")
        pass

    def test_search_field_by_name(cls): # aqui se encuentran las acciones o serie de acciones
        search_field = cls.driver.find_element_by_name("q")
        # pass

    def test_search_field_by_class_name(cls):
        search_field = cls.driver.find_element_by_class_name("input-text")# seleccionado de class="input-text required-entry" 

    def test_search_button_enable(cls):
        search_field = cls.driver.find_element_by_class_name("button")    

    @classmethod
    def tearDownClass(cls): # aqui se encuentran las acciones para finalizar
        cls.driver.quit() #por ejemplo cerrar el navegador para evitar una fuga de recursos

if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'hello-world-report'))