from playwright.sync_api import Page


def test_admin_panel_servicesList(auth_page: Page, BASE_URL):
    auth_page.goto(
        BASE_URL + "/admin-panel/servicesList?page_size=10&page=1",
        wait_until="networkidle",
    )

    locator = auth_page.locator("text=Название экскурсии")
    assert locator.count() == 1, locator.all()

    locator = auth_page.locator("text=Описание экскурсии")
    assert locator.count() == 1, locator.all()

    locator = auth_page.locator("text=Тип экскурсии")
    assert locator.count() == 1, locator.all()
