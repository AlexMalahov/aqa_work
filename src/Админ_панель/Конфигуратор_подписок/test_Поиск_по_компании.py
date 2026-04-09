from playwright.sync_api import Page


def test_admin_panel_monetizationSearch(auth_page: Page, BASE_URL):
    auth_page.goto(
        BASE_URL + "/admin-panel/monetizationSearch", wait_until="networkidle"
    )

    locator = auth_page.locator("text=Компания")
    assert locator.count() == 1, locator.all()
