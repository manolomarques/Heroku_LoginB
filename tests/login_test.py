import os
import pytest
from selenium.webdriver.chrome import webdriver
from pages.login_page import LoginPage


@pytest.fixture
def login(request):
    # _chromedriver = 'vendor/chromedriver.exe'
    _chromedriver = os.path.join(os.getcwd(), 'vendor', 'chromedriver.exe')

    if os.path.isfile(_chromedriver):
        driver_ = webdriver.Chrome(_chromedriver)

    else:
        driver_ = webdriver.Chrome()
        loginPage = LoginPage(driver_)

    def quit():
        driver_.quit() # desligar selenium

    # chamar o quit (a finalização)
    request.addfinalizer(quit)
    return loginPage

def testar_login_com_sucesso(login):
    # Faça o login com este usuário e senha
    login.com_('tomsmith', 'SuperSecretPassword!')
    # Validar o resultado = mensagem de sucesso presenta
    assert login.success_message_present()


def testar_login_com_usuario_invalido(login):
    login.com_('juca', 'SuperSecretPassword!')
    assert login.failure_message_present()


def testar_login_com_senha_invalida(login):
    login.com_('tomsmith', 'xpto1234')
    assert login.failure_message_present()
