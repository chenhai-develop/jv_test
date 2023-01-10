from appium import webdriver

class DriverUtils:
    __driver = None

    @classmethod
    def get_driver(cls):
        caps = {
            'platformName': 'Android',  # 被测手机是安卓
            'platformVersion': '12',  # 手机安卓版本
            'deviceName': 'OPPO',  # 设备名，安卓手机可以随意填写
            'appPackage': 'com.legrand.eliot',  # 启动APP Package名称
            'appActivity': 'com.legrand.eliot.business.SplashActivity',  # 启动Activity名称
            'unicodeKeyboard': False,  # 使用自带输入法，输入中文时填True
            'resetKeyboard': True,  # 执行完程序恢复原来输入法
            'noReset': False,  # 不要重置App，如果为False的话，执行完脚本后，app的数据会清空，比如你原本登录了，执行完脚本后就退出登录了
            'automationName': 'UiAutomator2'
        }
        if cls.__driver is None:
            cls.__driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
        return cls.__driver

    @classmethod
    def quit_driver(cls):
        if cls.get_driver() is not None:
            cls.get_driver().quit()
        cls.__driver = None


