import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_find_button_add_to_basket(browser, link, language):
    browser.get(link)
    time.sleep(30)
    assert browser.find_elements(By.CSS_SELECTOR, 'button.btn-add-to-basket'), "Button is not found"

