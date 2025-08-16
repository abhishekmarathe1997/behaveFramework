from selenium.webdriver.common.by import By

from features.utils.commonActions import CommonMethod


class loginpage(CommonMethod):

    def __init__(self, driver):
        super().__init__(driver)
        #self.driver = driver


    username_input = (By.NAME, "user_name")
    password_input = (By.NAME, "user_password")
    login_button = (By.NAME, "Login")
    logo_image = (By.XPATH, "//img[@src='include/images/vtiger-crm.gif']")
    Errormsg_text = (By.XPATH, "//*[contains(text(),'You must specify a valid username and password.')]")

    def login(self,userid,pwd):
        self.setUserid(userid)
        self.setPassword(pwd)
        self.click_login()

    def setUserid(self,userid):
        self.setInput(self.username_input,userid)

    def setPassword(self,pwd):
        self.setInput(self.password_input, pwd)

    def click_login(self):
        self.clickElement(self.login_button)

    def verifyLogo(self):
        try:
         return self.checkDisplay(self.logo_image)
        except:
            return False

    def verifyErrorMsg(self):
        return self.checkDisplay(self.Errormsg_text)
