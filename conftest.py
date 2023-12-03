import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def pytest_addoption(parser):
    parser.addoption("--language", action="store", default=None, help="Choose language: fr or es")

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(3)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.fixture(scope="function")
def language(request):
    return request.config.getoption("language")

@pytest.fixture(scope="function")
def link(language):
    base_url = "https://selenium1py.pythonanywhere.com"
    return f"{base_url}/{language}/catalogue/coders-at-work_207/"