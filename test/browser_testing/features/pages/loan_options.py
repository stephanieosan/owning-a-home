# coding: utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base import Base

# ELEMENTS ID
LOAN_AMOUNT = "loan-amount-value"
INTEREST_RATE = "loan-interest-value"

# ELEMENT CSS SELECTOR
LOAN_TERM_EXPAND = "#loan-term-expand-toggle"
LOAN_TERM_COLLAPSE = "#loan-term-expand-header + .expandable-content" + \
    ".expandable-hidden[style='display: block;'] .expand-close-link"
LOAN_TERM_SUBSECTION = "#loan-term-expand-header + .expandable-content." + \
    "expandable-hidden[style='display: block;'] .tight-heading"

INTEREST_RATE_EXPAND = "#interest-rate-expand-toggle"
INTEREST_RATE_STRUCTURE_SUBSECTION = "#interest-rate-expand-header + " + \
    ".expandable-content.expandable-hidden[style='display: block;'] " + \
    ".tight-heading"
INTEREST_RATE_STRUCTURE_COLLAPSE = "#interest-rate-expand-header + " + \
    ".expandable-content.expandable-hidden[style='display: block;'] " + \
    ".expand-close-link"

LOAN_TYPE_EXPAND = "#loan-programs-expand-toggle"
LOAN_TYPE_SUBSECTION = "#loan-programs-expand-header + .expandable-content" + \
    ".expandable-hidden[style='display: block;'] h3"
LOAN_TYPE_COLLAPSE = "#loan-programs-expand-header + .expandable-content" + \
    ".expandable-hidden[style='display: block;'] .expand-close-link"

SELECTED_TERM = ".term-timeline a.current .loan-length"


class LoanOptions(Base):

    def __init__(self, logger, directory, base_url=r'http://localhost/',
                 driver=None, driver_wait=10, delay_secs=0):
        super(LoanOptions, self).__init__(logger, directory, base_url,
                                          driver, driver_wait, delay_secs)
        self.logger = logger
        self.driver_wait = driver_wait

    def click_learn_more(self, page_section):
        if(page_section == 'Loan term'):
            e = self.driver.find_element_by_css_selector(LOAN_TERM_EXPAND)
        elif(page_section == 'Interest rate structure'):
            e = self.driver.find_element_by_css_selector(INTEREST_RATE_EXPAND)
        elif(page_section == 'Loan type'):
            e = self.driver.find_element_by_css_selector(LOAN_TYPE_EXPAND)
        else:
            raise Exception(page_section + " is NOT a valid section")
        e.click()

    def click_collapse(self, page_section):
        if(page_section == 'Loan term'):
            e_css = LOAN_TERM_COLLAPSE
        elif(page_section == 'Interest rate structure'):
            e_css = INTEREST_RATE_STRUCTURE_COLLAPSE
        elif(page_section == 'Loan type'):
            e_css = LOAN_TYPE_COLLAPSE
        else:
            raise Exception(page_section + " is NOT a valid section")

        msg = 'Element %s not found after %s secs' % (e_css, self.driver_wait)
        # Wait for the collapse button to appear
        element = WebDriverWait(self.driver, self.driver_wait)\
            .until(EC.element_to_be_clickable((By.CSS_SELECTOR, e_css)), msg)

        element.click()

    def get_subsection_text(self, page_section):
        local_wait = 2

        if(page_section == 'Loan term'):
            e_css = LOAN_TERM_SUBSECTION
        elif(page_section == 'Interest rate structure'):
            e_css = INTEREST_RATE_STRUCTURE_SUBSECTION
        elif(page_section == 'Loan type'):
            e_css = LOAN_TYPE_SUBSECTION
        else:
            raise Exception(page_section + " is NOT a valid section")

        msg = 'Element %s was not found after %s seconds' % (e_css, local_wait)
        try:
            # Wait for the subsection to expand
            element = WebDriverWait(self.driver, local_wait)\
                .until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                        e_css)), msg)
            return element.text
        except TimeoutException:
            return 'Section NOT visible'

    def get_expand_button_caption(self, page_section):
        if(page_section == 'Loan term'):
            e_css = LOAN_TERM_EXPAND
        elif(page_section == 'Interest rate structure'):
            e_css = INTEREST_RATE_EXPAND
        elif(page_section == 'Loan type'):
            e_css = LOAN_TYPE_EXPAND
        else:
            raise Exception(page_section + " is NOT a valid section")

        e_css = e_css + " .expandable-text"
        caption = self.driver.find_element_by_css_selector(e_css).text
        return caption

    def get_loan_amount(self):
        element = self.driver.find_element_by_id(LOAN_AMOUNT)
        return element.get_attribute("value")

    def get_interest_rate(self):
        element = self.driver.find_element_by_id(INTEREST_RATE)
        return element.get_attribute("value")

    def get_loan_term(self):
        element = self.driver.find_element_by_css_selector(SELECTED_TERM)
        return element.get_attribute("innerText")
