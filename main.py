import json
from HumanBehavior import *
from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from time import sleep


class GumtreeAdPoster:
    def __init__(self) -> None:
        self.configs = GumtreeAdPoster.read_configs()
        self.email = self.configs["email"]
        self.password = self.configs["password"]
        self.driver = GumtreeAdPoster.create_chrome_instance()
        self.login_page_url = "https://my.gumtree.com/login"
    
    @staticmethod
    def read_configs():
        with open("./configs.json", "r") as file:
            configs = json.loads(file.read())
            return configs
        
    @staticmethod
    def create_chrome_instance():
        chrome_options = ChromeOptions()
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        driver.maximize_window()
        stealth(driver,
            languages=["en-US", "en"],
            user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36',
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
        )
        return driver
    
    def gumtree_login(self):
        # XPATH FOR LOGIN ACCOUNT
        email_input_xpath = "//*[@id='email']"
        password_input_xpath = "//*[@id='fld-password']"
        login_button_xpath = "//*[@type='submit' and text()='Login']"
        
        self.driver.get(self.login_page_url)
        human_typer(self.driver,email_input_xpath,self.email)
        human_typer(self.driver,password_input_xpath,self.password)
        human_clicker_click(self.driver,login_button_xpath)
    
    
if __name__ == "__main__":
    glumtreeAdPoster = GumtreeAdPoster()
    glumtreeAdPoster.gumtree_login()
    