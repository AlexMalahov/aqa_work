from playwright.sync_api import Page


def test_admin_panel_bookingChart(auth_page: Page, BASE_URL):
    auth_page.goto(BASE_URL + "/admin-panel/bookingChart", wait_until="networkidle")

    locator = auth_page.locator("text=Пн")
    assert locator.count() == 1, locator.all()

    locator = auth_page.locator("text=Вт")
    assert locator.count() == 1, locator.all()

    locator = auth_page.locator("text=Ср")
    assert locator.count() == 1, locator.all()
