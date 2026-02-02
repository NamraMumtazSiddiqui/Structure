from selenium.webdriver.common.by import By

class LoginPage:

    # Locators
    username_field = (By.ID, "user-name")
    password_field = (By.ID, "password")
    login_button =   (By.ID, "login-button")

    # Constructor to use the driver from conftest.com fixture and store is to
    # self.driver=driver because every POM class needs a fixture (Browser Initialization) and other features to run tests
    # hence when the object of the class is created it gets automatically called
    # like login_page=LoginClass (driver)

    def __init__(self, driver):
        self.driver = driver

    def open_url(self):
        self.driver.get("https://www.saucedemo.com/")

    def enter_username(self, username):
        self.driver.find_element(*self.username_field).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
