from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class NoSuchElementException:
    pass


class BasePage:
    # função de inicialização da classe
    def __init__(self, driver):
        self.driver = driver

    # função para abrir uma pagina
    def _visitar(self, url):
        self.driver.get(url)

    # função generica de localicação de elemento
    def _procurar(self, locator):
        return self.driver.find_element(locator['by'], locator['value'])

    # função para clicar em um elemento
    def _click(self, locator):
        self._procurar(locator).click()

    # função para digitar em um elemento
    def _digitar(self, locator, input_text):
        self._procurar(locator).send_keys(input_text)

    # função para ler texto em um elemento
    def _ler(self, locator):
        self._procurar(locator).text()

    # função para ver se O ELEMENTO está visivel
    def _esta_visivel(self, locator, timeout=0):
        if timeout > 0:
            try:
                wait = WebDriverWait(self.driver, timeout)
                wait.until(
                    expected_conditions.visibility_of_element_located(
                        (locator['by'], locator['value'])
                    )
                )
            except TimeoutException:
                return False  # não encontrou o elemento
            return True  # encontrou o elemento
        else:
            try:
                return self._procurar(locator).is_displayed()
            except NoSuchElementException:
                return False
            # return True
