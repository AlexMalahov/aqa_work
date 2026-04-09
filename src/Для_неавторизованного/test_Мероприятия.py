from playwright.sync_api import Page, expect


def test_events(page: Page) -> None:
    page.goto("https://tourverse-dev.iwater-crm.online/")
    page.get_by_role("button", name="Мероприятия").first.click()
    expect(page.get_by_role("main")).to_contain_text("Партнеры:")
