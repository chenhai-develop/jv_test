import time
from app_test.log.myscreen import get_screen
import pytest
from app_test.data.ReadYaml import read_yaml
from app_test.page.login_page import LoginPage
from app_test.log.mylog import Logger
logger = Logger()
my_log = logger.get_log()

class TestLogin(LoginPage):
    def setup_class(self):
        my_log.debug('测试开始')

    @pytest.mark.parametrize('user,password', [(read_yaml('account', 'user'), read_yaml('account', 'password'))])
    def test01_login(self, user, password):
        if self.access().is_displayed():
            self.access().click()
        if self.access_confirm().is_displayed():
            self.access_confirm().click()
        my_log.debug('登录测试')
        my_log.debug(f"用户名输入:{user}")
        self.input_text(self.username(), user)
        my_log.debug(f"密码输入:{password}")
        self.input_text(self.password(), password)
        if self.agree().is_selected():
            my_log.debug('未勾选用户协议检查')
        else:
            my_log.debug('勾选用户协议检查')
            self.agree().click()
        time.sleep(5)
        self.login_button().click()
        my_log.debug('登录过程中截图')
        get_screen(self.get_driver())
        if self.access_confirm1().is_displayed():
            self.access_confirm1().click()
        try:
            self.navigation_my()
        except Exception as e:
            get_screen(self.get_driver())
            my_log.debug(f'检测元素失败:{e},截图')


    def teardown_class(self):
        my_log.debug('测试环境恢复')
        self.quit_driver()