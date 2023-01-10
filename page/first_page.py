from app_test.data.ReadYaml import read_yaml
from app_test.utils.BasePage import BasePage
from appium.webdriver.common.mobileby import MobileBy

class FirstPage(BasePage):
    def navigation_my(self):
        ele_value = read_yaml('firstPage', 'first_navigation_my')
        self.get_element(MobileBy.XPATH, f'//{ele_value}[contains(text(),"首页")]')


