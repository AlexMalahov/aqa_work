from playwright.sync_api import Page


def test_admin_panel_usersList(auth_page: Page, BASE_URL):
    auth_page.goto(
        BASE_URL + "/admin-panel/usersList?items_per_page=10&current_page=1",
        wait_until="networkidle",
    )

    locator = auth_page.locator("text=Фамилия")
    assert locator.count() == 1, locator.all()

    locator = auth_page.locator("text=Имя")
    assert locator.count() == 1, locator.all()

    locator = auth_page.locator("text=Отчество")
    assert locator.count() == 1, locator.all()
