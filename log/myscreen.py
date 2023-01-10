import datetime
import os.path



def get_screen(driver):
        local_path = os.path.dirname(__file__)+'\\screen_log'
        png_name = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')+'.png'
        file_path = os.path.join(local_path, png_name)
        driver.get_screenshot_as_file(file_path)




if __name__ == '__main__':
    get_screen()
