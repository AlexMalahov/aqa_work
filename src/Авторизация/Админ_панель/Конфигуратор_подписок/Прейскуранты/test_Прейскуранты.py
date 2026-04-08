from playwright.sync_api import Page


def test_admin_panel_priceList(auth_page: Page, BASE_URL):
    auth_page.goto(BASE_URL + "/admin-panel/priceList", wait_until="networkidle")

    locator = auth_page.locator("text=Приложение")
    assert locator.count() >= 1, locator.all()

    locator = auth_page.locator("text=Сценарии")
    assert locator.count() >= 1, locator.all()
    locator = auth_page.locator("text=Устройства")
    assert locator.count() >= 1, locator.all()