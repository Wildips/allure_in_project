import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be, have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_issue_name_with_dynamic_steps():
    allure.dynamic.tag("web")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Задачи в репозитории")
    allure.dynamic.story("Неавторизованный пользователь не может создать задачу в репозитории")
    allure.dynamic.link("https://github.com", name="Testing")
    with allure.step('Открываем главную страницу'):
        browser.open('/').wait_until(have.title('GitHub: Let\'s build from here'))

    with allure.step('Ищем репозиторий'):
        s('.header-search-button').with_(timeout=browser.config.timeout * 3).click()
        s('#query-builder-test').send_keys('eroshenkoam/allure-example')
        s('#query-builder-test').press_enter()

    with allure.step('Переходим по ссылке в репозиторий'):
        s(by.link_text('eroshenkoam/allure-example')).with_(timeout=browser.config.timeout * 3).click()

    with allure.step('Переходим на вкладку Задачи'):
        s("#issues-tab").with_(timeout=browser.config.timeout * 3).click()

    with allure.step('Проверяем имя тикета'):
        s(by.partial_text("#76")).should(be.visible)


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "eroshenkoam")
@allure.feature("Задачи в репозитории")
@allure.story("Авторизованный пользователь может создать задачу в репозитории")
@allure.link("https://github.com", name="Testing")
def test_issue_name_with_decorator_steps():
    # ARRANGE
    open_page()

    # ACTIONS
    search_for_repo('eroshenkoam/allure-example')
    open_repo('eroshenkoam/allure-example')
    open_issues_tab()

    # ASSERT
    check_issue_name()


@allure.step("Открываем главную страницу")
def open_page():
    browser.open('/').wait_until(have.title('GitHub: Let\'s build from here'))


@allure.step("Ищем репозиторий {repo}")
def search_for_repo(repo):
    s('.header-search-button').with_(timeout=browser.config.timeout * 3).click()
    s('#query-builder-test').send_keys(repo)
    s('#query-builder-test').press_enter()


@allure.step("Переходим по ссылке в репозиторий {repo}")
def open_repo(repo):
    s(by.link_text(repo)).with_(timeout=browser.config.timeout * 5).click()


@allure.step("Переходим на вкладку Задачи")
def open_issues_tab():
    s("#issues-tab").with_(timeout=browser.config.timeout * 3).click()


@allure.step("Проверяем имя тикета")
def check_issue_name():
    s(by.partial_text("#76")).should(be.visible)
