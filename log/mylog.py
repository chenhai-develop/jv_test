import logging
import os
import datetime
class Logger:
    def __init__(self):
        self.logger = logging.getLogger('JV')
        self.logger.setLevel(logging.DEBUG)

    def get_log(self, my_level=logging.DEBUG):
        t1 = datetime.datetime.now()
        file_name = t1.strftime('%Y-%m-%d-%H-%M-%S')
        local_path = os.path.dirname(__file__)+'\\file_log'
        # 文件路径
        file_path = os.path.join(local_path, file_name)

        # 文件处理器
        # ft = RotatingFileHandler(file_path, mode='a+', maxBytes=1,backupCount=3, encoding='utf-8')
        ft = logging.FileHandler(file_path, mode='a+', encoding='utf-8')
        ft.setLevel(my_level)

        # 控制台处理器
        st = logging.StreamHandler()
        st.setLevel(my_level)

        # 格式器
        my_format = logging.Formatter(fmt='%(asctime)s--->%(funcName)s--->%(levelname)s--->%(message)s')

        # 设置格式器
        ft.setFormatter(my_format)
        st.setFormatter(my_format)

        # 添加到日志
        self.logger.addHandler(ft)
        self.logger.addHandler(st)

        return self.logger


if __name__ == '__main__':
    logger = Logger()
    mylog = logger.get_log()






