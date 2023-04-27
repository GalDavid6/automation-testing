import pytest
import logging
import inspect
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class Setup:

    def getLogger(self):
        logger_name = inspect.stack()[1][3]  # setting the name as the name of the test_ that called that method
        logger = logging.getLogger(logger_name)
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        file_handler = logging.FileHandler("F:\\Projects\\PythonProjects\\SelAutomationTesting\\utilities\\logfile.log")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)  # filehandler object
        logger.setLevel(logging.DEBUG)  # showing info level msg and above
        """
        # printing to logger msgs at different levels
        logger.debug("A Debug statement is executed")
        logger.info("Information statement")
        logger.warning("Something is in warning mode")
        logger.error("A major error has happened")
        logger.critical("Critical issue")
        """
        return logger

    def verifyLinkPresence(self, text):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, text)))

    def selectOptionByText(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)


# This class meaning is to make the code more readable and clean instead of adding to every class test the line
# @pytest.mark.usefixtures("setup") every one of them will inheritance from this class, so they will be able to use
# the driver and also the class utilities
