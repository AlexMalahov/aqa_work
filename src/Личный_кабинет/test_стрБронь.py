from playwright.sync_api import Page


def test_my_booking_authorized(auth_page: Page, BASE_URL):
    auth_page.goto(BASE_URL + "/account/mybookings", wait_until="networkidle")
    locator = auth_page.locator("text=Мои бронирования")
    assert locator.count() == 2, locator.all()
