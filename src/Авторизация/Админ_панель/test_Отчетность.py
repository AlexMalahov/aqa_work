from playwright.sync_api import Page


def test_admin_panel_reports(auth_page: Page, BASE_URL):
    auth_page.goto(BASE_URL + "/admin-panel/reports", wait_until="networkidle")

    locator = auth_page.locator("text=Отчет о новых пользователях")
    assert locator.count() == 1, locator.all()

    locator = auth_page.locator("text=Отчет о новых клиентах")
    assert locator.count() == 1, locator.all()

    locator = auth_page.locator("text=Отчёт о запусках туров с различных устройств")
    assert locator.count() == 1, locator.all()
