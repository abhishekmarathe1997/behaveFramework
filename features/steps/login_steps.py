from behave import given, when, then
from selenium.webdriver.common.by import By

from features.Pages.HomePage import homepage
from features.Pages.LoginPage import loginpage


@given('user should be on login page')
def launchapp(context):
    context.driver.get("http://localhost:100")
    context.login_page = loginpage(context.driver)


@when('user enter the valid credentials')
def login(context):
    context.login_page.login("admin","admin")

@given('user should on home page')
def launch_login(context):
    context.driver.get("http://localhost:100")
    context.login_page = loginpage(context.driver)
    context.login_page.login("admin","admin")

@when('user enter the invalid credentials username as {userid} and password as {password}')
def login(context,userid,password):
    context.login_page.login(userid,password)

@then('user should navigated to home page')
def verifyHome(context):
    context.home_page = homepage(context.driver)
    context.home_page.verifyHome()


@when('user enter the invalid credentials')
def invalid_login(context):
    context.login_page.login("admin123","admin2424")

@then('user can see the error message')
def verifyerrormsg(context):
    context.login_page.verifyErrorMsg()

@then('user can logout')
def click_logout(context):
    context.home_page.click_logout()
