import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

class AddCustomer:
    # Add customer Page
    lnkCustomers_menu_xpath = "(//li[contains(@class,'treeview')]//span[text()='Users']/parent::a)[1]"  ## /parent::a => Click on the link (not Span)
    lnkCustomers_menuitem_xpath = "//ul[contains(@class,'treeview-menu')]//span[text()='Users']/parent::a"
    btnAddnew_xpath = "//a[contains(text(),'Create User')]"
    txtFirstName_xpath = "//input[@id='first_name']"
    txtLastName_xpath = "//input[@id='last_name']"
    txtEmail_xpath = "//input[@id='email']"
    ## Roles
    txtRoles_xpath = "//input[@id='roles[]-selectized']" ## OR //label[text()='Roles']/following-sibling::div//input
    txtPassword_xpath = "//input[@id='password']"
    txtConfirmPassword_xpath = "//input[@id='password_confirmation']"
    txtSaveButton_xpath = "//button[contains(text(),'Save')]"

    ## Initializer \ Constructor methods
    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_menu_xpath).click()

    def clickOnCustomersMenuItem(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_menuitem_xpath).click()

    def clickOnAddnew(self):
        self.driver.find_element_by_xpath(self.btnAddnew_xpath).click()

    def setFirstName(self, firstName):
        self.driver.find_element_by_xpath(self.txtFirstName_xpath).clear()
        self.driver.find_element_by_xpath(self.txtFirstName_xpath).send_keys(firstName)

    def setLastName(self, lastName):
        self.driver.find_element_by_xpath(self.txtLastName_xpath).clear()
        self.driver.find_element_by_xpath(self.txtLastName_xpath).send_keys(lastName)

    def setEmail(self, email):
        self.driver.find_element_by_xpath(self.txtEmail_xpath).clear()
        self.driver.find_element_by_xpath(self.txtEmail_xpath).send_keys(email)

    #Roles
    def setRole(self, roles):
        ##roles= ["Admin","Customer"]
        self.driver.find_element_by_xpath(self.txtRoles_xpath).clear()
        for role in roles:
            self.driver.find_element_by_xpath(self.txtRoles_xpath).send_keys(role)
            self.driver.find_element_by_xpath(self.txtRoles_xpath).send_keys(Keys.ENTER)

    def setPassword(self, password):
        self.driver.find_element_by_xpath(self.txtPassword_xpath).clear()
        self.driver.find_element_by_xpath(self.txtPassword_xpath).send_keys(password)

    def setConfirmPassword(self, ConfirmPassword):
        self.driver.find_element_by_xpath(self.txtConfirmPassword_xpath).clear()
        self.driver.find_element_by_xpath(self.txtConfirmPassword_xpath).send_keys(ConfirmPassword)

    def saveButton(self):
        self.driver.find_element_by_xpath(self.txtSaveButton_xpath).click()
