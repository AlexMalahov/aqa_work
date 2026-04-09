# from playwright.sync_api import Page


# def test_admin_panel_clientsList(auth_page: Page, BASE_URL):
#     auth_page.goto(BASE_URL + "/admin-panel/clientsList?page_size=10&page=1", wait_until="networkidle")

#     locator = auth_page.locator("text=Фамилия")
#     assert locator.count() == 1, locator.all()

#     locator = auth_page.locator("text=Имя")
#     assert locator.count() == 1, locator.all()

#     locator = auth_page.locator("text=Отчество")
#     assert locator.count() == 1, locator.all()
