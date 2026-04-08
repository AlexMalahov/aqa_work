from playwright.sync_api import Page


def test_excursions_exist(page: Page, BASE_URL):
    page.goto(BASE_URL, wait_until="networkidle")
    locator = page.locator(
        "text=VR-экскурсия с эффектом полного погружения в музее ГОН"
    )
    assert locator.count() == 1, "❌ Нет доступных экскурсий"
