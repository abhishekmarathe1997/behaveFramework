from selenium.webdriver.common.by import By

from features.utils.commonActions import CommonMethod


class homepage(CommonMethod):

    def __init__(self, driver):
        super().__init__(driver)
        #self.driver = driver

    home_link = (By.LINK_TEXT, "Home")
    logout_link = (By.LINK_TEXT, "Logout")
    NewLead_link = (By.LINK_TEXT, "New Lead")




    def verifyHome(self):
        print("hello")
        return self.checkDisplay(self.home_link)

    def verifyLogout(self):
        print("hello")
        return self.checkDisplay(self.logout_link)

    def click_logout(self):
        self.clickElement(self.logout_link)

    def click_NewLead(self):
        self.clickElement(self.NewLead_link)

