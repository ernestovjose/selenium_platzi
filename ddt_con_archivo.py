import csv, unittest
from ddt import ddt, data, unpack
from selenium import webdriver

def get_data(file_name):
    rows = []
    data_file = open(file_name, "r")
    reader = csv.reader(data_file)
    next(reader, None)

    for row in reader:
        rows.append(row)
    return rows


@ddt
class SearchDDT(unittest.TestCase):

    def setUp(self): # aqui se prepara el entorno para la prueba
        self.driver = webdriver.Chrome(executable_path= r'./chromedriver.exe')
        driver = self.driver #Reasignamos la variable para invocarla mas facil
        driver.maximize_window() #esto ayuda en caso de que los elmentos cambien se posicion al maximizar la ventana
        driver.get('http://demo-store.seleniumacademy.com/')

    @data(*get_data('testdata.csv'))    
    @unpack #despaquetara estas duplas

    def test_ddt(self, search_value, expected_count):
        driver = self.driver

        search_field = driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys(search_value)
        search_field.submit()

        products = driver.find_elements_by_xpath('//h2[@class="product-name"]/a') #manera de escribir manualmente un xpath
        print(products)
        expected_count = int(expected_count)
        print(expected_count)

        if expected_count > 0:
            self.assertEqual(expected_count, len(products))
        else:
            message = driver.find_element_by_class_name('note-msg')
            self.assertEqual('Your search returns no results.', message)

        print(f'Found {len(products)} products')    

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity = 2)