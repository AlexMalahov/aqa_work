from playwright.sync_api import Page


def test_admin_panel_rolesList(auth_page: Page, BASE_URL):
    auth_page.goto(
        BASE_URL + "/admin-panel/rolesList?items_per_page=10&current_page=1",
        wait_until="networkidle",
    )

    locator = auth_page.locator("text=Название роли")
    assert locator.count() == 1, locator.all()

    locator = auth_page.locator("text=Доступные разделы")
    assert locator.count() == 1, locator.all()

    locator = auth_page.locator("text=Уровень доступа")
    assert locator.count() == 1, locator.all()
