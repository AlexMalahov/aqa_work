from playwright.sync_api import Page


def test_admin_panel_dashbord(auth_page: Page, BASE_URL):
    auth_page.goto(BASE_URL + "/admin-panel/dashboard", wait_until="networkidle")

    locator = auth_page.locator("text=Общая статистика")
    assert locator.count() == 1, locator.all()

    locator = auth_page.locator("text=Статистика запуска сценариев")
    assert locator.count() == 1, locator.all()
    
    locator = auth_page.locator("text=Самые популярные сценарии")
    assert locator.count() == 1, locator.all()

    locator = auth_page.locator("text=Статистика бронирований")
    assert locator.count() == 1, locator.all()

    locator = auth_page.locator("text=Самые популярные экскурсии")
    assert locator.count() == 1, locator.all()
