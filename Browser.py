from selenium import webdriver
import pickle
import sys

class Browser():
    def __init__(self, driver=False) -> None:
        if driver:
            self.driver = driver
        else:
            self.open()
            self.driver.minimize_window()

    def open(self, path="./chrome/chromedriver"):
        '''Open Browser by path'''
        path = path+".exe" if sys.platform == "win32" else path
        self.driver = webdriver.Chrome(path)

    def open_site(self, url):
        self.driver.get(url)

    def save(self, file_name):
        '''Saved coockie driver'''
        pickle.dump(self.driver.get_cookies(), open(file_name + ".pkl", "wb"))

    def load(self, file_name):
        cookies = pickle.load(open(file_name + ".pkl", "rb"))
        for cookie in cookies:
            self.driver.add_cookie(cookie)
