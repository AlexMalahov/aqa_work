from playwright.sync_api import Page, expect


def test_news(page: Page) -> None:
    page.goto("https://tourverse-dev.iwater-crm.online/")
    page.get_by_role("button", name="СМИ о нас").first.click()
    expect(page.get_by_role("heading", name="СМИ о нас")).to_be_visible()
    page.locator(".slick-arrow.slick-next > svg").click()
