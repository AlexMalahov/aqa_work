from playwright.sync_api import Page


def test_admin_panel_newsList(auth_page: Page, BASE_URL):
    auth_page.goto(BASE_URL + "/admin-panel/newsList?page_size=10&page=1", wait_until="networkidle")

    locator = auth_page.locator("text=Заголовок")
    assert locator.count() == 1, locator.all()

    locator = auth_page.locator("text=Текст новости")
    assert locator.count() == 1, locator.all()

    locator = auth_page.locator("text=Дата новости")
    assert locator.count() == 1, locator.all()
