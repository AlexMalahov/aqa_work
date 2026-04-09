from playwright.sync_api import Page


def test_admin_panel_reviewsList(auth_page: Page, BASE_URL):
    auth_page.goto(BASE_URL + "/admin-panel/reviewsList?page_size=10&page=1", wait_until="networkidle")

    locator = auth_page.locator("text=Наименование услуги")
    assert locator.count() == 1, locator.all()

    locator = auth_page.locator("text=Дата создания")
    assert locator.count() == 1, locator.all()

    locator = auth_page.locator("text=Дата обновления")
    assert locator.count() == 1, locator.all()
