import pytest
from playwright.sync_api import sync_playwright, BrowserContext


def test_room_authorized(auth_page: BrowserContext, BASE_URL, EMAIL):
    auth_page.goto(BASE_URL + "/account", wait_until="networkidle")
    locator = auth_page.locator(f"text={EMAIL}")
    assert locator.count() == 1, locator.all()
