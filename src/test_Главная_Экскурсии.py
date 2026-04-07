import pytest
from playwright.sync_api import sync_playwright, BrowserContext


def test_excursions_exist(page: BrowserContext, BASE_URL):
    page.goto(BASE_URL, wait_until="networkidle")
    locator = page.locator(
        "text=VR-экскурсия с эффектом полного погружения в музее ГОН"
    )
    assert locator.count() == 1, "❌ Нет доступных экскурсий"
