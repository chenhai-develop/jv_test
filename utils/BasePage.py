from jv_test.utils.BaseUtils import DriverUtils
from selenium.webdriver.support.wait import WebDriverWait
class BasePage(DriverUtils):


    def get_element(self, ele_type, ele_value):
        wait = WebDriverWait(self.get_driver(), 10)
        ele = wait.until(lambda x: x.find_element(ele_type, ele_value))
        return ele

    def input_text(self, ele, text):
        ele.send_keys(text)