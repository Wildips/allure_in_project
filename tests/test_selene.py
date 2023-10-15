from selene.support import by
from selene.support.conditions import be, have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_issue_name():
    # ARRANGE
    browser.open('/').wait_until(have.title('GitHub: Let\'s build from here'))

    # ACTIONS
    s('.header-search-button').with_(timeout=browser.config.timeout * 3).click()
    s('#query-builder-test').send_keys('eroshenkoam/allure-example')
    s('#query-builder-test').press_enter()

    s(by.link_text('eroshenkoam/allure-example')).with_(timeout=browser.config.timeout * 5).click()

    s("#issues-tab").with_(timeout=browser.config.timeout * 3).click()

    # ASSERT
    s(by.partial_text("#76")).should(be.visible)
