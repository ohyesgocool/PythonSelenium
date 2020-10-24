from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):

    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN = (By.ID, "password - login - button")



    def __init__(self,driver):
        super.__init__(self,driver)


