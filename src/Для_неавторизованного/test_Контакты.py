from playwright.sync_api import Page, expect


def test_contacts(page: Page) -> None:
    page.goto("https://tourverse-dev.iwater-crm.online/")
    page.get_by_role("button", name="Контакты").first.click()
    expect(page.get_by_text("ИП:", exact=True)).to_be_visible()
    page.get_by_role("heading", name="Контакты").click()
    expect(page.get_by_role("heading", name="Контакты")).to_be_visible()
    expect(page.get_by_text("ИНН:")).to_be_visible()
    expect(page.get_by_text("ОГРНИП:")).to_be_visible()
    expect(page.get_by_text("Телефон:")).to_be_visible()
    expect(page.get_by_text("Почтовый адрес:")).to_be_visible()
    expect(page.get_by_text("Email:")).to_be_visible()
    expect(page.get_by_text("Техподдержка:")).to_be_visible()
    expect(page.get_by_role("heading")).to_contain_text("Контакты")
    expect(page.get_by_role("main")).to_contain_text("ИП:")
    expect(page.get_by_role("main")).to_contain_text("ИНН:")
    expect(page.get_by_role("main")).to_contain_text("ОГРНИП:")
    expect(page.get_by_role("main")).to_contain_text("Телефон:")
    expect(page.get_by_role("main")).to_contain_text("Почтовый адрес:")
    expect(page.get_by_role("main")).to_contain_text("Email:")
    expect(page.get_by_role("main")).to_contain_text("Техподдержка:")
