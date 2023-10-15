from selene.support import by
from selene.support.conditions import be, have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

browser.config.timeout = 2.0

REPO_NAME = 'eroshenkoam/allure-example'


def test_issue_name():
    # ARRANGE
    browser.open('https://github.com').driver.maximize_window()
    browser.wait_until(have.title('GitHub: Let\'s build from here'))

    # ACTIONS
    s('.header-search-button').click()
    s('#query-builder-test').send_keys(REPO_NAME)
    s('#query-builder-test').press_enter()

    s(by.link_text(REPO_NAME)).with_(timeout=browser.config.timeout * 3).click()

    s("#issues-tab").with_(timeout=browser.config.timeout * 3).click()

    # ASSERT
    s(by.partial_text("#76")).should(be.visible)
