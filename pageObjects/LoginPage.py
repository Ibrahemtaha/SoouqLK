class LoginPage:
    textbox_username_id = "email"
    textbox_password_xpath = "//input[@name='password']"
    button_login_xpath = "//button[contains(text(),'Login')]"
    link_logout1_xpath1 = "//span[contains(text(),'Test')]" #//span[contains(text(),'Test')]
    link_logout2_xpath2 = "//a[contains(text(),'Logout')]"

    def __init__(self, driver):
        self.driver = driver
    #
    def setUserName(self, username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_xpath(self.textbox_password_xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_password_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element_by_xpath(self.link_logout1_xpath1).click()
        self.driver.find_element_by_xpath(self.link_logout2_xpath2).click()

    ### Login in one Method instead of 3 mthods #####
    def loginOneStep(self, username, password):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)
        self.driver.find_element_by_xpath(self.textbox_password_xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_password_xpath).send_keys(password)
        self.driver.find_element_by_xpath(self.button_login_xpath).click()



