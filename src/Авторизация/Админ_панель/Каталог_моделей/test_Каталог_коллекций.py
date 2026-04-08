from playwright.sync_api import Page


def test_admin_panel_3dModelsList(auth_page: Page, BASE_URL):
    auth_page.goto(BASE_URL + "/admin-panel/modelCollection", wait_until="networkidle")

    locator = auth_page.locator("text=Название коллекции")
    assert locator.count() == 1, locator.all()

    locator = auth_page.locator("text=Теги")
    assert locator.count() == 1, locator.all()

    locator = auth_page.locator("text=Категории")
    assert locator.count() == 1, locator.all()
