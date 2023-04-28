import pytest

from pageObjects.HomePage import HomePage
from testsData.testsData import TestData
from utilities.Setup import Setup


class TestE2E(Setup):

    def test_FillingFormAndPurchase(self, getData):
        log = self.getLogger()
        home_page = HomePage(self.driver)
        home_page.getName().send_keys(getData["fullname"])
        home_page.getEmail().send_keys(getData["email"])
        home_page.getPassword().send_keys(getData["password"])
        home_page.getLoveIceCream().click()
        self.selectOptionByText(home_page.getGender(), getData["gender"])
        home_page.selectRadioByText(home_page.getStatus(), getData["status"])
        home_page.getCalender().send_keys(getData["bday"])
        home_page.submitForm()
        msg = home_page.getSuccessMessage().text
        assert "Success" in msg
        log.info("Successfully filled the form")
        log.info(msg)

        checkout_page = home_page.shopItems()
        cards = checkout_page.getCardsTitle()
        i = -1
        log.info("Adding Blackberry to cart")
        for card in cards:
            i = i + 1
            if card.text == getData["device"]:
                checkout_page.getCardsFooter()[i].click()
                break
        log.info("Added Blackberry, and processing to payment page")
        confirm_page = checkout_page.checkoutItems()
        confirm_page.getConfirm().click()
        confirm_page.getCountry().send_keys(getData["country"])
        self.verifyLinkPresence(getData["country"]).click()
        log.info("Entered country name")
        confirm_page.getTerms().click()
        confirm_page.getPurchase().click()
        msg = confirm_page.getSuccessMessage().text
        assert "Success" in msg
        log.info("Purchase success")

    @pytest.fixture(params=TestData.getTestData("test_FillingFormAndPurchase"))
    def getData(self, request):
        return request.param