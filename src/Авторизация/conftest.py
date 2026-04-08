import time

import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def auth_page(BASE_URL, EMAIL, PASSWORD):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # лучше False для отладки
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

        browser.close()


"""@pytest.fixture(scope="function")
def auth_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(storage_state="auth_state.json")
        page = context.new_page()
        yield page
        browser.close()"""
