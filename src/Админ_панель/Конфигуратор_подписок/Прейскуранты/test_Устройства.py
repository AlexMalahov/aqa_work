from playwright.sync_api import Page


def test_admin_panel_equipment(auth_page: Page, BASE_URL):
    auth_page.goto(
        BASE_URL + "/admin-panel/priceList/equipment", wait_until="networkidle"
    )

    locator = auth_page.locator("text=Цена")
    assert locator.count() == 1, locator.all()

    locator = auth_page.locator("text=Описание")
    assert locator.count() == 1, locator.all()
    locator = auth_page.locator("text=Период")
    assert locator.count() == 1, locator.all()
