import pytest

from pageObjects.HomePage import HomePage
from testsData.testsData import TestData
from utilities.Setup import Setup


class TestHomePage(Setup):

    def test_FormSubmission(self, getData):
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

    def test_GoToShop(self):
        home_page = HomePage(self.driver)
        home_page.shopItems()

    @pytest.fixture(params=TestData.getTestData("test_FormSubmission"))
    def getData(self, request):
        return request.param
