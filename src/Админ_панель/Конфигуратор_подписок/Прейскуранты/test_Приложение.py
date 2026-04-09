import time

from playwright.sync_api import Page


def test_admin_panel_app(auth_page: Page, BASE_URL):
    auth_page.goto(BASE_URL + "/admin-panel/priceList/app", wait_until="networkidle")
    time.sleep(1)
    locator = auth_page.locator("text=Цена")
    assert locator.count() >= 5, (locator.all(), 1)

    locator = auth_page.locator("text=Описание")
    assert locator.count() >= 1, (locator.all(), 2)

    locator = auth_page.locator("text=Период")
    assert locator.count() >= 1, (locator.all(), 3)
