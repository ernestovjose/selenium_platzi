import unittest
from selenium import webdriver

class RegisterNewUser(unittest.TestCase):

    def setUp(self): # aqui se prepara el entorno para la prueba
        self.driver = webdriver.Chrome()
        driver = self.driver #Reasignamos la variable para invocarla mas facil
        driver.implicitly_wait(2)
        driver.maximize_window() #esto ayuda en caso de que los elmentos cambien se posicion al maximizar la ventana
        driver.get('http://demo-store.seleniumacademy.com/')

    def test_new_user(self):
        driver = self.driver
        driver.find_element_by_xpath('/html/body/div/div[2]/header/div/div[2]/div/a/span[2]').click() #para que el menu despliegue
        driver.find_element_by_link_text('Log In').click()

        create_account_button = driver.find_element_by_xpath('//*[@id="login-form"]/div/div[1]/div[2]/a/span/span')
        self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled()) #determina si el boton esta visible y habilitado
        create_account_button.click()

        self.assertEqual('Create New Customer Account', driver.title) #verificamos si el sitio web es el correcto por el titulo ingresado

        first_name = driver.find_element_by_id('firstname')
        middle_name = driver.find_element_by_id('middlename')
        last_name = driver.find_element_by_id('lastname')
        email_address = driver.find_element_by_id('email_address')
        password = driver.find_element_by_id('password')
        confirm_password = driver.find_element_by_id('confirmation')
        news_letter_subscription = driver.find_element_by_id('is_subscribed')
        submit_button = driver.find_element_by_xpath('//*[@id="form-validate"]/div[2]/button')

        self.assertTrue(first_name.is_enabled() 
        and middle_name.is_enabled()
        and last_name.is_enabled()
        and email_address.is_enabled()
        and password.is_enabled()
        and confirm_password.is_enabled()
        and news_letter_subscription.is_enabled()
        and submit_button.is_enabled())

        first_name.send_keys('Lola')
        middle_name.send_keys('Perez')
        last_name.send_keys('Cardona')
        email_address.send_keys('cardona@gmail.com')
        password.send_keys('123')
        confirm_password.send_keys('123')
        submit_button.click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity = 2)