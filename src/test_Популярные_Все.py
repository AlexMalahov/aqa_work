import pytest
from playwright.sync_api import sync_playwright, BrowserContext


def test_excursions_exist(page: BrowserContext, BASE_URL):
    page.goto(BASE_URL + "/popular", wait_until="networkidle")
    locator = page.locator(
        'text=Интерактивный тур "Ганзейская ярмарка в Великом Новгороде" (в очках дополненной реальности)'
    )
    assert locator.count() == 1, "❌ Нет доступных экскурсий"
