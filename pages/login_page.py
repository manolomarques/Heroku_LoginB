from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    _username_input = {'by': By.ID, 'value': 'username'}
    _password_input = {'by': By.ID, 'value': 'password'}
    _submit_button = {'by': By.CSS_SELECTOR, 'value': 'button.radius'}
    _failure_message = {'by': By.CSS_SELECTOR, 'value': '.flash.error'}
    _success_message = {'by': By.CSS_SELECTOR, 'value': '.flash.success'}
    _login_form = {'by': By.CSS_SELECTOR, 'value': 'login'}

    # ações possiveis na pagina

    # método de inicialização
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self._visitar('https://the-internet.herokuapp.com/login')
        assert self._esta_visivel(self._login_form, 5)
    def com_(self, username, password):
        self._digitar(self._username_input, username)
        self._digitar(self._password_input, password)
