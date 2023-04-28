# Selenium Python testing automation

![Project Image](https://media.licdn.com/dms/image/C5616AQG7a6ROuQs_PA/profile-displaybackgroundimage-shrink_350_1400/0/1654021659209?e=1687996800&v=beta&t=cGT05Mylrk_TTYFYqsm3zsinFEMs1ZTS1W03SNw_Yb0)

-> The purpose of the project was to practice converting test cases to automata using Selenium and Pytest
     while using OOP to write readable and clean code.
     After the tests are performed HTML, log, and screenshots files are produced automatically
     (Screenshots will be taken only when a test failed from the section that failed for follow-up).

* The project run on a local Jenkin server, which I can easily manage without using an IDE or CMD (optional).
---
## Libraries

- Selenium 
- WebDriver
- Pytest
- OpenPyXL
- Logging 
- Inspect

---
## Project structure

- PageObjects -> hold a Class for each page on the website, helps us to get elements of each page. 
	- CheckoutPage.py
	- ConfirmPage.py
	- HomePage.py

- Reports -> The HTML report from the tests produce here.
	- report.html

- Tests -> All test cases are divided into files according to tests for pages and E2E.
	- test_CheckoutPage.py
	- test_HomePage.py
	- test_E2E
	- screenshots from failed tests
	- conftest.py (instead of copy default line code as config necceseray for each test,
		 with pytest fixture i'm doing that once and using in class utilities.Setup)
	
- TestsData -> holding a xlsx file with data and parameters for each test 
	     and class with a method to extract the data for each test.
	-testsData.py
	-TestsData.xlsx

- Utilites -> 
	- Setup.py - reuseable class that hold reuseable methods, logger, and default setttings for each test.
	- logfile.log

---
## How To Use

1. download drivers Chromedriver(Chrome), Geckodriver(Firefox), and msedgedriver(EdgeDriver)
2. install all mention above libararies.
3. Make sure all path in files are updated according to your computer 

---
## Author Info

- Github - [GalDavid6](https://github.com/GalDavid6)
- Linkedin - [Gal David](https://www.linkedin.com/in/gal-david-22871a182/)

[Back To The Top](#Selenium-Python-testing-automation)