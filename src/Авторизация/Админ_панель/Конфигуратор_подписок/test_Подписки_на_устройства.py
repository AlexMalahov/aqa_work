from playwright.sync_api import Page


def test_admin_panel_monetizationEquipment(auth_page: Page, BASE_URL):
    auth_page.goto(BASE_URL + "/admin-panel/monetizationEquipment?page_size=10&page=1", wait_until="networkidle")

    locator = auth_page.locator("text=Краткое наименование компании")
    assert locator.count() == 1, locator.all()

    locator = auth_page.locator("text=Наименование устройства")
    assert locator.count() == 1, locator.all()