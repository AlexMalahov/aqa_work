from playwright.sync_api import Page


def test_admin_panel_notifications(auth_page: Page, BASE_URL):
    auth_page.goto(BASE_URL + "/admin-panel/notifications?item_per_page=10&current_page=1", wait_until="networkidle")

    locator = auth_page.locator("text=Тема уведомления")
    assert locator.count() == 1, locator.all()

    locator = auth_page.locator("text=Тип уведомления")
    assert locator.count() == 1, locator.all()

    locator = auth_page.locator("text=Канал уведомления")
    assert locator.count() == 1, locator.all()
