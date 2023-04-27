from selenium.webdriver.common.by import By
from pageObjects.CheckoutPage import CheckoutPage


class HomePage:
    shop = (By.LINK_TEXT, "Shop")
    name = (By.NAME, "name")
    email = (By.NAME, "email")
    password = (By.ID, 'exampleInputPassword1')
    check_button = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    status = (By.CSS_SELECTOR, "[class*='form-check-inline']")
    calendar = (By.CSS_SELECTOR, "input[name='bday']")
    submit = (By.CSS_SELECTOR, "input[type='submit']")
    alert_message = (By.CSS_SELECTOR, "[class*='alert-success']")

    def __init__(self, driver):
        self.driver = driver

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        return CheckoutPage(self.driver)

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def getLoveIceCream(self):
        return self.driver.find_element(*HomePage.check_button)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def getStatus(self):
        return self.driver.find_elements(*HomePage.status)

    def selectRadioByText(self, locator, text):
        for loc in locator:
            if loc.find_element(By.CLASS_NAME, "form-check-label").text == text:
                loc.find_element(By.CLASS_NAME, "form-check-input").click()
                break

    def getCalender(self):
        return self.driver.find_element(*HomePage.calendar)

    def submitForm(self):
        self.driver.find_element(*HomePage.submit).click()

    def getSuccessMessage(self):
        return self.driver.find_element(*HomePage.alert_message)

