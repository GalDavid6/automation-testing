import pytest

from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.HomePage import HomePage
from testsData.testsData import TestData
from utilities.Setup import Setup


class TestCheckoutPage(Setup):

    def test_addItem(self, getData):
        log = self.getLogger()
        home_page = HomePage(self.driver)
        checkout_page = home_page.shopItems()
        cards = checkout_page.getCardsTitle()
        i = -1
        for card in cards:
            i = i + 1
            log.info(card.text)
            if card.text == getData["device"]:
                log.info(getData["device"])
                checkout_page.getCardsFooter()[i].click()
                break

    def test_checkoutItems(self):
        home_page = HomePage(self.driver)
        checkout_page = home_page.shopItems()
        checkout_page.checkoutItems()

    @pytest.fixture(params=TestData.getTestData("test_addItem"))
    def getData(self, request):
        return request.param