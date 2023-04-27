from selenium.webdriver.common.by import By
from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:

    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    checkout = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    def __init__(self, driver):
        self.driver = driver

    def getCardsTitle(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)

    def getCardsFooter(self):
        return self.driver.find_elements(*CheckoutPage.cardFooter)

    def checkoutItems(self):
        self.driver.find_element(*CheckoutPage.checkout).click()
        return ConfirmPage(self.driver)

