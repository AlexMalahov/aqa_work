from playwright.sync_api import Page


def test_admin_panel_productsList(auth_page: Page, BASE_URL):
    auth_page.goto(
        BASE_URL + "/admin-panel/productsList?page_size=10&page=1",
        wait_until="networkidle",
    )

    locator = auth_page.locator("text=Наименование коллекции")
    assert locator.count() == 1, locator.all()

    locator = auth_page.locator("text=Описание коллекции")
    assert locator.count() == 1, locator.all()

    locator = auth_page.locator("text=Статус")
    assert locator.count() == 1, locator.all()
