from po_lesson.pages.main_page import MainPage
from po_lesson.pages.login_page import LoginPage


def test_open_login_page(browser):
    main_page = MainPage(browser)
    main_page.open_base_page()
    main_page.open_login_page()
    login_page = LoginPage(browser)
    login_page.should_be_login_page()
