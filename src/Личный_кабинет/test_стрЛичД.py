from playwright.sync_api import Page


def test_room_authorized(auth_page: Page, BASE_URL, EMAIL):
    auth_page.goto(BASE_URL + "/account", wait_until="networkidle")
    locator = auth_page.locator(f"text={EMAIL}")
    assert locator.count() == 1, locator.all()
