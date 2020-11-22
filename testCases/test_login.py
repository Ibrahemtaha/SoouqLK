import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.ReadProperties import ReadConfig
from utilities.customerLogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    ### Calling the loggen method from LogGen Class ####
    logger= LogGen.loggen()

    ##### 1) test_homePageTitle ######
    def test_homePageTitle(self,setup):
        self.logger.info("*************** Test_001_Login *****************")
        self.logger.info("****Verify Home page title test ****")
        self.driver = setup
        self.driver.get(self.baseURL)

        act_title=self.driver.title
        if act_title == "Login - FleetCart":
            assert True
            self.driver.close()
            self.logger.info("*************** HomePageTitle test is passed *****************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.info("*************** HomePageTitle test is Failed *****************")
            assert False

        ######## 2) test_login #########
    def test_login(self,setup):
        self.logger.info("*************** test_login test is passed *****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        ### To access the methos in "pageObjects.LoginPage import LoginPage" Class
        self.lp = LoginPage(self.driver)
        self.lp.loginOneStep(self.username,self.password)
        # self.lp.setUserName(self.username)
        # self.lp.setPassword(self.password)
        # self.lp.clickLogin()

        act_title = self.driver.title
        if act_title == "Dashboard - FleetCart Admin":
            assert True
            self.driver.close()
            self.logger.info("*************** test_login test is passed *****************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            self.driver.close()
            self.logger.error("*************** test_login test is Failed *****************")
            assert False

    ##### 3) test_logout ######
    def test_logout(self,setup):
        self.logger.info("*************** test_logout test is passed *****************")

        self.driver = setup
        self.driver.get(self.baseURL)
        ### To access the methos in "pageObjects.LoginPage import LoginPage" Class
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.lp.clickLogout()

        act_title = self.driver.title
        if act_title.strip() == "Login - FleetCart":  ##Trim\Strip (remove the white space in the Tag)
            assert True
            self.driver.close()
            self.logger.info("*************** test_logout test is passed *****************")

        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_logout.png")
            self.driver.close()
            self.logger.error("*************** test_logout test is Failed *****************")

            assert False

