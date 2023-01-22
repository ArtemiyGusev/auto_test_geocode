import os
from dotenv import load_dotenv
from selene.support.shared.jquery_style import s
from auto_test_geocode.controls.helper.ui_tests_helper import url_open_size
from auto_test_geocode.controls.submit import submit


def open_page_and_login(url='/', width=1920, height=1080):
    url_open_size(url, width, height)
    load_dotenv()

    def login(email=os.getenv('EMAIL_GEOCODE'), password=os.getenv('PASSWORD_GEOCODE')):

        form_login = s('#kc-form-login')

        form_login.s('#username').type(email)
        form_login.s('#password').type(password)
        form_login.s('#kc-login').click()
        submit(form_login.s('#kc-login')).submit_button_click()

    login()
