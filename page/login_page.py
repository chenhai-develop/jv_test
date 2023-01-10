
from jv_test.data.ReadYaml import read_yaml
from jv_test.utils.BasePage import BasePage
from appium.webdriver.common.mobileby import MobileBy
class LoginPage(BasePage):
    def access(self):
        ele_value = read_yaml('permissionDialog', 'button1')
        return self.get_element(MobileBy.ID, ele_value)

    def access_confirm(self):
        ele_value = read_yaml('permissionDialog', 'confirm')
        return self.get_element(MobileBy.ID, ele_value)

    def access_confirm1(self):
        ele_value = read_yaml('permissionDialog', 'permission_allow')
        return self.get_element(MobileBy.ID, ele_value)

    def username(self):
        ele_value = read_yaml('loginPage', 'user_element')
        return self.get_element(MobileBy.ID, ele_value)

    def password(self):
        ele_value1 = read_yaml('loginPage', 'password_element')
        return self.get_element(MobileBy.ID, ele_value1)

    def login_button(self):
        ele_value2 = read_yaml('loginPage', 'loginbutton_element')
        return self.get_element(MobileBy.ID, ele_value2)

    def agree(self):
        ele_value3 = read_yaml('loginPage', 'agree_element_element')
        return self.get_element(MobileBy.ID, ele_value3)

    def navigation_my(self):

        self.get_element(MobileBy.XPATH, '//*[@resource-id="com.legrand.eliot:id/text"][@text="首页"]')



if __name__ == '__main__':
    pass
