import pytest
from playwright.sync_api import sync_playwright, BrowserContext


def test_my_booking_authorized(auth_page: BrowserContext, BASE_URL):
    auth_page.goto(BASE_URL + "/account/mybookings", wait_until="networkidle")
    locator = auth_page.locator("text=Мои бронирования")
    assert locator.count() == 2, locator.all()
