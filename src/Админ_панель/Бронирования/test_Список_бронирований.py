from playwright.sync_api import Page


def test_admin_panel_bookingsList(auth_page: Page, BASE_URL):
    auth_page.goto(
        BASE_URL
        + "/admin-panel/bookingsList?date_from=01.04.2026&date_to=30.04.2026&page_size=10&page=1",
        wait_until="networkidle",
    )

    locator = auth_page.locator("text=Название экскурсии")
    assert locator.count() == 1, locator.all()

    locator = auth_page.locator("text=Компания")
    assert locator.count() == 1, locator.all()

    locator = auth_page.locator("text=В ожидании подтверждения")
    assert locator.count() == 1, locator.all()
