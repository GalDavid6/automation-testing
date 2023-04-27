import pytest
from selenium import webdriver
driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="Browser. Valid options are Chrome, Firefox and Edge"
    )
# addoption goal is to let us store from cmd which browser the user want to work with and later use it in our program
# to open the specific browser


@pytest.fixture(scope="class")
def setup(request):
    # before:
    global driver
    browser_name = request.config.getoption('browser_name')
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="F:\\Users\\User\\SeleniumDrivers\\chromedriver.exe")
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="F:\\Users\\User\\SeleniumDrivers\\geckodriver.exe")
    elif browser_name == "edge":
        driver = webdriver.Edge(executable_path="F:\\Users\\User\\SeleniumDrivers\\msedgedriver.exe")
    else:
        print("no support for the required browser")
        exit()
    driver.implicitly_wait(5)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    # assign the driver we created to cls(class) later wherever we will use setup in our program
    # we will be able to use driver
    yield
    # yield is like splitting the code "run" into two (before yield and after) when we reach yield line all fixture
    # with "setup" will run and when they are done the program will return to here where is stops
    # after:
    driver.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)

