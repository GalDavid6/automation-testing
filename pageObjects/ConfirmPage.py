from selenium.webdriver.common.by import By


class ConfirmPage:

    confirm = (By.CSS_SELECTOR, "[class*='btn btn-success']")
    country = (By.ID, "country")
    terms = (By.CSS_SELECTOR, "[class*='checkbox checkbox-primary']")
    purchase = (By.CSS_SELECTOR, "input[value='Purchase']")
    alert = (By.CSS_SELECTOR, "[class*='alert alert-success alert-dismissible']")

    def __init__(self, driver):
        self.driver = driver

    def getConfirm(self):
        return self.driver.find_element(*ConfirmPage.confirm)

    def getCountry(self):
        return self.driver.find_element(*ConfirmPage.country)

    def getTerms(self):
        return self.driver.find_element(*ConfirmPage.terms)

    def getPurchase(self):
        return self.driver.find_element(*ConfirmPage.purchase)

    def getSuccessMessage(self):
        return self.driver.find_element(*ConfirmPage.alert)