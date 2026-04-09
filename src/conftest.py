import os
import time
import pytest
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture(scope="session", autouse=True)
def BASE_URL():
    return os.environ["BASE_URL"]


@pytest.fixture(scope="session", autouse=True)
def EMAIL():
    return os.environ["EMAIL"]


@pytest.fixture(scope="session", autouse=True)
def PASSWORD():
    return os.environ["PASSWORD"]


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture(scope="session")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page


@pytest.fixture(scope="session")
def auth_page(BASE_URL, EMAIL, PASSWORD, browser):
    context = browser.new_context()
    page = context.new_page()

    # 👉 Открываем страницу логина
    page.goto(BASE_URL + "/login", wait_until="networkidle")

    # 👉 Вводим логин / пароль
    page.fill('input[id="login"]', EMAIL)
    page.fill('input[id="password"]', PASSWORD)

    # 👉 Нажимаем кнопку входа
    page.click('button[type="submit"]')

    # 👉 Ждём успешную авторизацию (редирект или элемент)
    page.wait_for_load_state("networkidle")
    time.sleep(10)
    # context.storage_state(path="auth_state.json")
    # browser.close()
    yield page
