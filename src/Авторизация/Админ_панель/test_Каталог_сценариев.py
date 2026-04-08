from playwright.sync_api import Page


def test_admin_panel_sceneCatalog(auth_page: Page, BASE_URL):
    auth_page.goto(BASE_URL + "/admin-panel/sceneCatalog", wait_until="networkidle")

    locator = auth_page.locator("text=Название сценария")
    assert locator.count() == 1, locator.all()

    locator = auth_page.locator("text=Владелец сценария")
    assert locator.count() == 1, locator.all()

    locator = auth_page.locator("text=Тип девайса")
    assert locator.count() == 1, locator.all()
