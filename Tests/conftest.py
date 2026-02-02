import os
from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

SCREENSHOT_FOLDER="Screenshots"

@pytest.fixture(scope="session")

# To use same function multiple times like Open Broweser , Maximize Window and Implicit Wait and Quit the Browser !
def driver():

    # Service is a class, which acts as a middleman between Selenium and ChromeDriver.
    # We Initialize Chrome Browser via Chrome Driver

    #Service                           Class
    #driver1                            Object(instance)
    #webdriver.Chrome(...)              CLass



    driver_path = r"C:\Users\HP\Downloads\Chromedrivers\Drivers\chromedriver.exe"
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()  # optional, makes browser fullscreen

    yield driver

    # Before Yield , its Setup and after yield its teardown to close the browser
    # Before yield = Setup
    # After yield = Teardown

    driver.quit()
    

def take_screenshot(driver, name):
    os.makedirs(SCREENSHOT_FOLDER, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filepath = os.path.join(SCREENSHOT_FOLDER, f"{name}_{timestamp}.png")

    driver.save_screenshot(filepath)

# Hooks automatically gets called at a specific event like to generate pass/fail screenshots
# to generate reports after test
# 1-pytest_runtest_setup
# test start hone se pehle run hota hai
# 2-pytest_runtest_makereport
# 3-pytest_sessionfinish

# ✅ Hook: Runs after every test
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    driver = item.funcargs.get("driver", None)

    if driver is not None and report.when == "call":
        if report.failed:
            take_screenshot(driver, item.name + "_FAIL")
