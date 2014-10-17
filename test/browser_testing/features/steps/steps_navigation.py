from behave import given, when, then
from hamcrest.core import assert_that
from hamcrest.library.text.stringcontains import contains_string

from pages.home import Home
from pages.base import Base

# XPATH LOCATORS
OWNING_A_HOME = "//li/a[@href='../']"
LOAN_COMPARISON = "//li/a[@href='../loan-comparison/']"
LOAN_OPTIONS = "//li/a[@href='../loan-options/']"
RATE_CHECKER = "//li/a[@href='../rate-checker/']"

# RELATIVE URL'S
RELATIVE_URL_HOME = 'index.html'
RELATIVE_URL_LC = 'loan-comparison'
RELATIVE_URL_LT = 'loan-options'
RELATIVE_URL_RC = 'rate-checker'


@given(u'I navigate to the "{page_name}" page')
def step(context, page_name):
    if (page_name == 'Owning a Home'):
        context.base.go(RELATIVE_URL_HOME)
    elif (page_name == 'Loan Comparison'):
        context.base.go(RELATIVE_URL_LC)
    elif (page_name == 'Loan Options'):
        context.base.go(RELATIVE_URL_LT)
    elif (page_name == 'Rate Checker'):
        context.base.go(RELATIVE_URL_RC)
    else:
        raise Exception(page_name + ' is NOT a valid page')


@given(u'I navigate to the Demo OAH page')
def step(context):
    context.base.go()


@when(u'I click on the "{link_name}" link')
def step(context, link_name):
    # Click the requested tab
    if (link_name == 'Owning a Home'):
        context.navigation.click_link(OWNING_A_HOME)
    elif (link_name == 'Loan Comparison'):
        context.navigation.click_link(LOAN_COMPARISON)
    elif (link_name == 'Loan Options'):
        context.navigation.click_link(LOAN_OPTIONS)
    elif (link_name == 'Rate Checker'):
        context.navigation.click_link(RATE_CHECKER)
        context.base.sleep(3)  # This is troubleshoot an error in Jenkins
    else:
        raise Exception(link_name + ' is NOT a valid link')


@then(u'I should see "{link_name}" displayed in the page title')
def step(context, link_name):
    # Verify that the page title matches the link we clicked
    context.base.sleep(2)
    page_title = context.base.get_page_title()
    assert_that(page_title, contains_string(link_name))


@then(u'I should see the page scroll to the "{page_anchor}" section')
def step(context, page_anchor):
    current_url = context.base.get_current_url()
    assert_that(current_url, contains_string(page_anchor))
