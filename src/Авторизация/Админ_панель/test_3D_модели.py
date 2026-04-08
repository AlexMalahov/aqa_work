from playwright.sync_api import Page


def test_admin_panel_3dModelsList(auth_page: Page, BASE_URL):
    auth_page.goto(BASE_URL + "/admin-panel/3dModelsList?page_size=10&page=1", wait_until="networkidle")

    locator = auth_page.locator("text=Категория модели")
    assert locator.count() == 1, locator.all()

    locator = auth_page.locator("text=Наименование модели")
    assert locator.count() == 1, locator.all()

    locator = auth_page.locator("text=Описание модели")
    assert locator.count() == 1, locator.all()
