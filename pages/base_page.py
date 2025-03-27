from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def find_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def click_element(self, locator, timeout=10):
        self.find_element(locator, timeout).click()

    def enter_text(self, locator, text, timeout=10):
        self.find_element(locator, timeout).send_keys(text)

    def wait_for_element_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def wait_for_element_invisible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def scroll_to_element(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def transition_to_next_tub(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def transition_to_previous_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
