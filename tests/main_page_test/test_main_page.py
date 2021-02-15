from po_lesson.pages.main_page import MainPage


def test_click_sing_in_button(browser):
    main_page = MainPage(browser)
    main_page.open_base_page()
    main_page.open_login_page()

