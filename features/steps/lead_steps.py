from behave import given, when, then
from selenium.webdriver.common.by import By

from features.Pages.HomePage import homepage
from features.Pages.LeadPage import leadpage
from features.Pages.LoginPage import loginpage


@when('user click on new Lead')
def clicknewlead(context):
    context.home_page = homepage(context.driver)
    context.home_page.click_NewLead()


@when('user fills the mandatory fields and click save')
def createlead(context):
    context.lead_page = leadpage(context.driver)
    context.lead_page.create_lead("Modi","BJP")

@then('lead should be created successfully')
def verifyLead(context):
    pass


@when("user create multiple leads and verified")
def step_create_multiple_leads(context):
    # Iterate over table rows
    for row in context.table:
        firstname = row['firstname']
        lastname = row['lastname']
        context.home_page = homepage(context.driver)
        context.home_page.click_NewLead()
        context.lead_page = leadpage(context.driver)
        context.lead_page.create_lead(firstname,lastname)