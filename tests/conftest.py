import pytest
import json
import allure
from selene.support.shared import browser
from allure import attachment_type


@pytest.fixture(scope="session", autouse=True)
def browser_binding():
    browser.config.base_url = 'https://github.com'
    browser.config.timeout = 2.0
    browser.driver.maximize_window()

    yield browser

    browser.quit()


@pytest.fixture(scope='function', autouse=True)
def artifacts_creation():
    yield
    allure.attach("Text content", name="Text", attachment_type=attachment_type.TEXT)
    allure.attach("<h1>Hello, world</h1>", name="Html", attachment_type=attachment_type.HTML)
    allure.attach(json.dumps({"first": 1, "second": 2}), name="Json", attachment_type=attachment_type.JSON)
