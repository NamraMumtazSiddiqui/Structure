import pytest
from POM.login_page import LoginPage

def test_login(driver):

    login_page = LoginPage(driver)
    login_page.open_url()
    login_page.login("standard_user", "secreat_sauce")

    title = driver.getTitle()
    print("Title", title)
    source = driver.getPageSource()
    print("Title", source)
    url = driver.getCurrentUrl()
    print("Title", url)


def test_asserturl(driver):
    assert "source" in driver.current_url

