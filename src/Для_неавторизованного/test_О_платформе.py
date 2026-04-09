from playwright.sync_api import Page, expect


def test_aboutUs(page: Page) -> None:
    page.goto("https://tourverse-dev.iwater-crm.online/")
    page.get_by_role("button", name="О платформе").first.click()
    expect(page.locator("body")).to_contain_text(
        "Универсальная многофункциональная платформа, предназначенная для размещения AR/VR приложений."
    )
    expect(page.locator("body")).to_contain_text("Сферы применения платформы")
    expect(page.locator("body")).to_contain_text("Культура и искусство")
    expect(page.locator("body")).to_contain_text("Туризм и путешествия")
    expect(page.locator("body")).to_contain_text("Образование и обучение")
    expect(page.locator("body")).to_contain_text(
        "Функциональные характеристики Tourverse"
    )
    expect(page.locator("body")).to_contain_text("Стоимость")
    expect(page.locator("body")).to_contain_text(
        "Для получения консультации о тарифах и условиях:"
    )
