import selenium
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC


class BasePage:

    def __init__(self , driver):
        self.driver = driver


    def click(self , locator ):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locator)).click()


driver = selenium.webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.google.com/")
driver.find_element(By.ID , "input").send_keys("Naveen automation labs")

