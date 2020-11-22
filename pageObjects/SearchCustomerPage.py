class SearchCustomer():
    # Add customer Page
    labelSearch_xpath = "//label[contains(text(),'Search:')]"

    tblSearchResults_xpath="//table[@id='DataTables_Table_0']"
    table_xpath="//table[@id='customers-grid']"
    tableRows_xpath="//table[@id='customers-grid']//tbody/tr"
    tableRows_xpath="//tbody/tr"
    tableColumns_xpath="//table[@id='customers-grid']//tbody/tr/td"
    tableColumns_xpath="//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def setSearch(self,search):
        self.driver.find_element_by_xpath(self.labelSearch_xpath).clear()
        self.driver.find_element_by_xpath(self.labelSearch_xpath).send_keys(search)

    def getNoOfRows(self):
        return len(self.driver.find_elements_by_xpath(self.tableRows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements_by_xpath(self.tableColumns_xpath))

    def searchCustomerByEmail(self,email):
        flag=False
        for r in range(1,self.getNoOfRows()+1):
          table=self.driver.find_element_by_xpath(self.table_xpath)
          emailid=table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
          if emailid == email:
              flag = True
              break
        return flag

    def searchCustomerByName(self,Name):
        flag=False
        for r in range(1,self.getNoOfRows()+1):
          table=self.driver.find_element_by_xpath(self.table_xpath)
          name=table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text
          if name == Name:
              flag = True
              break
        return flag
