import unittest #esta libreria para hacer pruebas unitarias en python
from pyunitreport import HTMLTestRunner #Permite hacer reportes que seran escritos en un html
from selenium import webdriver #Y este permite llamar al driver del exporador que vamos a utilizar

class HelloWorld(unittest.TestCase):

    @classmethod # Al declarar un class method todas las pruebas se realizan en el navegador
    def setUpClass(cls): # aqui se prepara el entorno para la prueba
        cls.driver = webdriver.Chrome()
        driver = cls.driver #Reasignamos la variable para invocarla mas facil
        driver.implicitly_wait(10) #Aqui indicamos que espere 10 seg antes de tomar alguna accion
    
    def test_hello_world(cls): # aqui se encuentran las acciones o serie de acciones
        driver = cls.driver
        driver.get('http://10.36.237.137/')
        pass

    def test_hello_youtube(cls): #Debe empezar por la palabra test
        driver = cls.driver
        driver.get('https://www.youtube.com/') #llamamos al sitio Web
        pass

    @classmethod
    def tearDownClass(cls): # aqui se encuentran las acciones para finalizar
        cls.driver.quit() #por ejemplo cerrar el navegador para evitar una fuga de recursos

if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'hello-world-report'))