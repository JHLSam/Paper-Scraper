from selenium import webdriver
import selenium
import os

"""
For ignoring unsecure connections
custom = webdriver.ChromeOptions()
custom.add_argument('--ignore-ssl-errors=yes')
custom.add_argument('--ignore-certificate-errors')
"""
class CustomFileError(RuntimeError):
    def __init__(self,existing_dir):
        self.existing_dir = existing_dir

def screencap(DRIVER_PATH,url,screenshot_name):
    driver = webdriver.Chrome(DRIVER_PATH)#(DRIVER_PATH,options = custom) for SSL certificate ignore 
    driver.get(url)
    driver.execute_script('document.body.style.zoom = "50%"')
    storage_folder = "Screenshots_storage"
    for root,dirs,files in os.walk(os.getcwd(), topdown=True):
        for files in dirs:
            print(files)
            print(type(files))
            if files != storage_folder:
                os.mkdir(storage_folder)
            else:
                try:
                    os.mkdir(storage_folder)
                except FileExistsError:
                    print("Folder already exists! Directory not created")
                screenshot = driver.save_screenshot("Screenshots_storage/" + screenshot_name)
                return driver.quit()
            
"""
DRIVER_PATH = os.getcwd() + "/chromedriver"
screencap(DRIVER_PATH,"https://www.yahoo.com","screenshots.png")
"""
